import requests
import logging
from app.core.config import GEMINI_API_KEY
from .prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

class GeminiClientError(Exception):
    pass

class AIConfigurationError(Exception):
    pass

class GeminiClient:
    @staticmethod
    def _get_headers():
        if not GEMINI_API_KEY:
            raise AIConfigurationError("GEMINI_API_KEY is missing from environment variables.")
        return {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }

    @staticmethod
    def chat_with_tools(messages, tools=None):
        try:
            headers = GeminiClient._get_headers()
            
            # Ensure system prompt is the first message
            if not messages or messages[0].get("role") != "system":
                messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
                
            payload = {
                "model": "gemini-2.5-flash",
                "messages": messages,
                "temperature": 0.3
            }
            
            if tools:
                payload["tools"] = tools
                payload["tool_choice"] = "auto"
                
            response = requests.post(GEMINI_API_URL, json=payload, headers=headers, timeout=15)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.Timeout:
            logger.error("Gemini API request timed out.")
            raise GeminiClientError("The AI service timed out.")
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"Gemini API request failed. Status: {e.response.status_code}. Response: {e.response.text}")
            else:
                logger.error(f"Gemini API request failed: {e}")
            raise GeminiClientError("The AI service encountered an error.")
        except (GeminiClientError, AIConfigurationError):
            raise
        except Exception as e:
            logger.error(f"Unexpected error in GeminiClient: {e}")
            raise GeminiClientError("An internal AI service error occurred.")
