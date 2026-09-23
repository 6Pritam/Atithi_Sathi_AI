import logging
from app.core.config import AI_PROVIDER
from app.ai.gemini_client import GeminiClient, GeminiClientError
from app.ai.grok_client import GrokClient, GrokClientError

logger = logging.getLogger(__name__)

class AIServiceError(Exception):
    pass

class AIProvider:
    @staticmethod
    def chat_with_tools(messages, tools=None):
        try:
            if AI_PROVIDER == "gemini":
                logger.info(f"AI Provider: Gemini | Model: gemini-1.5-flash | Request: START")
                response = GeminiClient.chat_with_tools(messages, tools)
                logger.info("AI Provider: Gemini | Request: SUCCESS")
                return response
            elif AI_PROVIDER == "grok":
                logger.info("AI Provider: Grok | Model: grok-2 | Request: START")
                response = GrokClient.chat_with_tools(messages, tools)
                logger.info("AI Provider: Grok | Request: SUCCESS")
                return response
            else:
                logger.error(f"Unknown AI_PROVIDER configured: {AI_PROVIDER}")
                raise AIServiceError("Invalid AI provider configuration.")
        except (GeminiClientError, GrokClientError) as e:
            logger.error(f"AI Provider ({AI_PROVIDER}) Request: FAILED | Error: {e}")
            raise AIServiceError("The AI service encountered an error.")
        except Exception as e:
            logger.error(f"Unexpected error in AIProvider: {e}")
            raise AIServiceError("An internal AI service error occurred.")
