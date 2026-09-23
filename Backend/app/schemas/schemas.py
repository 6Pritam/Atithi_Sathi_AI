from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict, Any

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        v_stripped = v.strip()
        if not v_stripped:
            raise ValueError('message cannot be empty')
        if len(v_stripped) > 2000:
            raise ValueError('message is too long')
        return v_stripped

class ErrorDetail(BaseModel):
    code: str
    message: str

class ChatResponse(BaseModel):
    success: bool
    conversation_id: Optional[str] = None
    message: Optional[str] = None
    attachments: Optional[List[Dict[str, Any]]] = []
    tool_state: Optional[str] = None
    error: Optional[ErrorDetail] = None

class HealthResponse(BaseModel):
    status: str
    service: str
