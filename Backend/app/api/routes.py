from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import uuid
import json
import logging
from datetime import datetime, timezone
from app.models.database import get_db
from app.models.models import Conversation, Message
from app.schemas.schemas import ChatRequest, ChatResponse, HealthResponse, ErrorDetail
from app.ai.provider import AIProvider, AIServiceError
from app.tools.database_tools import (
    TOOL_DEFINITIONS, get_hotel_details, search_hotels, get_hotel_policy, check_availability, search_web
)

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "ok", "service": "atithi-saathi-ai"}

@router.get("/health/db")
def health_check_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "service": "database"}
    except Exception as e:
        logger.error(f"DB Health check failed: {e}")
        return {"status": "error", "service": "database"}

@router.get("/history")
def get_recent_conversations(db: Session = Depends(get_db)):
    convs = db.query(Conversation).order_by(Conversation.updated_at.desc()).limit(20).all()
    return [{"id": c.id, "title": c.title, "updated_at": c.updated_at} for c in convs]

@router.get("/history/{conversation_id}")
def get_conversation_history(conversation_id: str, db: Session = Depends(get_db)):
    conv = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
        
    messages = db.query(Message).filter(Message.conversation_id == conversation_id).order_by(Message.created_at.asc()).all()
    
    return {
        "conversation_id": conv.id,
        "title": conv.title,
        "messages": [
            {
                "id": m.id,
                "sender": m.sender,
                "content": m.content,
                "created_at": m.created_at
            } for m in messages
        ]
    }

def format_attachments(tool_name: str, tool_result: dict):
    # Map backend fields to frontend expected fields based on tool used
    attachments = []
    
    if tool_name == "search_hotels" and "hotels" in tool_result:
        frontend_hotels = []
        for h in tool_result["hotels"]:
            frontend_hotels.append({
                "id": h["id"],
                "name": h["name"],
                "imageSrc": h["image_url"],
                "rating": h["rating"],
                "reviews": str(h["review_count"]),
                "location": h["location"],
                "distanceInfo": h["distance_info"],
                "amenities": h["amenities"][:2] if h["amenities"] else [],
                "price": f"₹{int(h['base_price']):,}",
                "totalInfo": f"₹{int(h['base_price']) * 2:,} total" # Mock total for frontend
            })
        if frontend_hotels:
            attachments.append({
                "type": "hotel_list",
                "data": frontend_hotels
            })
            
    elif tool_name == "get_hotel_details" and "rooms" in tool_result:
        frontend_hotel = {
            "id": tool_result["id"],
            "name": tool_result["name"],
            "imageSrc": tool_result["image_url"],
            "rating": tool_result["rating"],
            "reviews": str(tool_result["review_count"]),
            "location": tool_result["location"],
            "distanceInfo": tool_result["distance_info"],
            "amenities": tool_result["amenities"],
            "price": f"₹{int(tool_result['base_price']):,}",
            "description": tool_result.get("description", "")
        }
        attachments.append({
            "type": "hotel",
            "data": [frontend_hotel]
        })
        
    elif tool_name == "check_availability" and tool_result.get("available"):
        frontend_rooms = []
        for r in tool_result["rooms"]:
            frontend_rooms.append({
                "id": r["category"],
                "name": r["category"],
                "price": f"₹{int(r['price_per_night']):,}",
                "max_guests": r["max_guests"],
                "amenities": r["amenities"]
            })
        if frontend_rooms:
            attachments.append({
                "type": "room",
                "data": frontend_rooms
            })
            
    return attachments

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    logger.info(f"chat request conversation_id={request.conversation_id}")
    
    # 1. Load/Create Conversation
    if request.conversation_id:
        conversation = db.query(Conversation).filter(Conversation.id == request.conversation_id).first()
        if not conversation:
            return ChatResponse(
                success=False,
                error=ErrorDetail(code="CONVERSATION_NOT_FOUND", message="Conversation not found")
            )
    else:
        conversation = Conversation(id=f"conv_{uuid.uuid4().hex[:12]}", title=request.message[:30])
        db.add(conversation)
        db.commit()
    
    # 2. Save User Message
    user_msg = Message(
        conversation_id=conversation.id,
        sender="user",
        content=request.message
    )
    db.add(user_msg)
    db.commit()
    
    # 3. Load Context
    recent_msgs = db.query(Message).filter(Message.conversation_id == conversation.id).order_by(Message.created_at.desc()).limit(10).all()
    recent_msgs.reverse() # Oldest first in the slice
    
    grok_messages = []
    for msg in recent_msgs:
        role = "user" if msg.sender == "user" else "assistant"
        grok_messages.append({"role": role, "content": msg.content})
        
    # 4. Call AI
    try:
        ai_response = AIProvider.chat_with_tools(grok_messages, tools=TOOL_DEFINITIONS)
    except AIServiceError as e:
        logger.error(f"AI Service Error: {e}")
        return ChatResponse(success=False, error=ErrorDetail(code="AI_SERVICE_ERROR", message=str(e)))
    except Exception as e:
        logger.error(f"Unexpected Error during chat: {e}")
        return ChatResponse(success=False, error=ErrorDetail(code="INTERNAL_ERROR", message="An unexpected error occurred."))
        
    response_message = ai_response["choices"][0]["message"]
    
    tool_state = None
    attachments = []
    
    # 5. Handle Tool Calls
    if response_message.get("tool_calls"):
        tool_call = response_message["tool_calls"][0]
        function_name = tool_call["function"]["name"]
        arguments = json.loads(tool_call["function"]["arguments"])
        
        logger.info(f"tool={function_name} args={arguments}")
        tool_state = f"Executing {function_name}..."
        
        tool_result = {}
        if function_name == "search_hotels":
            tool_result = search_hotels(db, **arguments)
        elif function_name == "get_hotel_details":
            tool_result = get_hotel_details(db, **arguments)
        elif function_name == "get_hotel_policy":
            tool_result = get_hotel_policy(db, **arguments)
        elif function_name == "check_availability":
            tool_result = check_availability(db, **arguments)
        elif function_name == "search_web":
            tool_result = search_web(**arguments)
            
        attachments = format_attachments(function_name, tool_result)
        
        # Append tool call and result to messages and call AI again
        grok_messages.append(response_message)
        grok_messages.append({
            "role": "tool",
            "tool_call_id": tool_call["id"],
            "name": function_name,
            "content": json.dumps(tool_result)
        })
        
        try:
            second_response = AIProvider.chat_with_tools(grok_messages)
            logger.info(f"Second response: {second_response}")
            
            final_message = second_response["choices"][0]["message"].get("content")
            if final_message is None:
                final_message = "I am unable to process that."
        except AIServiceError as e:
            logger.error(f"AI Service Error: {e}")
            return ChatResponse(success=False, error=ErrorDetail(code="AI_SERVICE_ERROR", message=str(e)))
        except Exception as e:
            logger.error(f"Unexpected Error during chat: {e}")
            return ChatResponse(success=False, error=ErrorDetail(code="INTERNAL_ERROR", message="An unexpected error occurred."))
    else:
        final_message = response_message.get("content", "I am unable to process that.")
        
    # 6. Save AI Message
    ai_msg = Message(
        conversation_id=conversation.id,
        sender="ai",
        content=final_message,
        attached_data=attachments
    )
    db.add(ai_msg)
    
    conversation.updated_at = datetime.now(timezone.utc)
    db.commit()
    
    logger.info(f"chat completed conversation_id={conversation.id}")
    
    return ChatResponse(
        success=True,
        conversation_id=conversation.id,
        message=final_message,
        attachments=attachments,
        tool_state=None
    )
