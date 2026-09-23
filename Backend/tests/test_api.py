import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app
import json

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health_db():
    response = client.get("/api/v1/health/db")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat_empty_message():
    response = client.post("/api/v1/chat", json={"message": "   "})
    assert response.status_code == 422
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"

@patch("app.api.routes.GrokClient.chat_with_tools")
def test_chat_new_conversation(mock_chat):
    mock_chat.return_value = {
        "choices": [{"message": {"content": "Hello! I am Atithi Saathi AI."}}]
    }
    
    response = client.post("/api/v1/chat", json={"message": "Hi"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["conversation_id"] is not None
    assert data["message"] == "Hello! I am Atithi Saathi AI."

@patch("app.api.routes.GrokClient.chat_with_tools")
def test_chat_existing_conversation(mock_chat):
    mock_chat.return_value = {
        "choices": [{"message": {"content": "First response"}}]
    }
    
    # First request
    res1 = client.post("/api/v1/chat", json={"message": "Hi"})
    conv_id = res1.json()["conversation_id"]
    
    # Second request
    mock_chat.return_value = {
        "choices": [{"message": {"content": "Second response"}}]
    }
    res2 = client.post("/api/v1/chat", json={"message": "Follow up", "conversation_id": conv_id})
    assert res2.status_code == 200
    assert res2.json()["conversation_id"] == conv_id
    assert res2.json()["message"] == "Second response"

    # Test history
    res3 = client.get(f"/api/v1/history/{conv_id}")
    assert res3.status_code == 200
    history = res3.json()
    assert len(history["messages"]) == 4

@patch("app.api.routes.GrokClient.chat_with_tools")
def test_chat_hotel_search(mock_chat):
    # Mocking first grok call returning a tool call
    mock_chat.side_effect = [
        {
            "choices": [{"message": {
                "content": None,
                "tool_calls": [{
                    "id": "call_123",
                    "function": {
                        "name": "search_hotels",
                        "arguments": json.dumps({"location": "BLR"})
                    }
                }]
            }}]
        },
        # Mocking second grok call returning final string
        {
            "choices": [{"message": {"content": "Here are some hotels in Bangalore."}}]
        }
    ]
    
    response = client.post("/api/v1/chat", json={"message": "Find me a hotel in Bangalore"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["attachments"]) > 0
    assert data["attachments"][0]["type"] == "hotel_list"
    assert data["message"] == "Here are some hotels in Bangalore."

@patch("app.api.routes.GrokClient.chat_with_tools")
def test_chat_availability_success(mock_chat):
    mock_chat.side_effect = [
        {
            "choices": [{"message": {
                "content": None,
                "tool_calls": [{
                    "id": "call_124",
                    "function": {
                        "name": "check_availability",
                        "arguments": json.dumps({"hotel_id": "h_1", "check_in": "2030-10-10", "check_out": "2030-10-15", "adults": 2})
                    }
                }]
            }}]
        },
        {
            "choices": [{"message": {"content": "Yes, rooms are available."}}]
        }
    ]
    
    response = client.post("/api/v1/chat", json={"message": "Is Grand Horizon available?"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["attachments"]) > 0
    assert data["attachments"][0]["type"] == "room"

@patch("app.api.routes.GrokClient._get_headers")
def test_ai_missing_key(mock_headers):
    from app.ai.grok_client import AIConfigurationError
    mock_headers.side_effect = AIConfigurationError("GROK_API_KEY is missing from environment variables.")
    
    response = client.post("/api/v1/chat", json={"message": "Hello"})
    assert response.status_code == 503
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "AI_NOT_CONFIGURED"
