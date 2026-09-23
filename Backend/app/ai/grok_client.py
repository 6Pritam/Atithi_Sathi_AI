import requests
import json
import logging
from app.core.config import GROK_API_KEY
from .prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)

GROK_API_URL = "https://api.x.ai/v1/chat/completions"

class GrokClientError(Exception):
    pass

class AIConfigurationError(Exception):
    pass

class GrokClient:
    @staticmethod
    def _get_headers():
        if not GROK_API_KEY:
            raise AIConfigurationError("GROK_API_KEY is missing from environment variables.")
        return {
            "Authorization": f"Bearer {GROK_API_KEY}",
            "Content-Type": "application/json"
        }

    @staticmethod
    def chat_with_tools(messages, tools=None):
        try:
            headers = GrokClient._get_headers()
            
            # Ensure system prompt is the first message
            if not messages or messages[0].get("role") != "system":
                messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
                
            payload = {
                "model": "grok-2",
                "messages": messages,
                "temperature": 0.3
            }
            
            if tools:
                payload["tools"] = tools
                payload["tool_choice"] = "auto"
                
            response = requests.post(GROK_API_URL, json=payload, headers=headers, timeout=15)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.Timeout:
            logger.error("Grok API request timed out.")
            raise GrokClientError("The AI service timed out.")
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"Grok API request failed. Status: {e.response.status_code}. Response: {e.response.text}")
            else:
                logger.error(f"Grok API request failed: {e}")
            raise GrokClientError("The AI service encountered an error.")
        except (GrokClientError, AIConfigurationError):
            raise
        except Exception as e:
            logger.error(f"Unexpected error in GrokClient: {e}")
            raise GrokClientError("An internal AI service error occurred.")
