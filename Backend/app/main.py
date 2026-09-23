from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.routes import router
from app.core.config import FRONTEND_URL
from app.ai.grok_client import GrokClientError, AIConfigurationError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Atithi Saathi AI Backend")

# Properly configure CORS based on environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": str(exc)
            }
        },
    )

@app.exception_handler(AIConfigurationError)
async def ai_config_exception_handler(request: Request, exc: AIConfigurationError):
    return JSONResponse(
        status_code=503,
        content={
            "success": False,
            "error": {
                "code": "AI_NOT_CONFIGURED",
                "message": "The AI service is not configured."
            }
        },
    )

@app.exception_handler(GrokClientError)
async def grok_client_exception_handler(request: Request, exc: GrokClientError):
    return JSONResponse(
        status_code=502,
        content={
            "success": False,
            "error": {
                "code": "AI_SERVICE_ERROR",
                "message": str(exc)
            }
        },
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Internal server error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "An internal server error occurred."
            }
        },
    )
