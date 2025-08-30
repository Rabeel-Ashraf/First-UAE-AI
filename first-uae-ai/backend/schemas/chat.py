# backend/schemas/chat.py
from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    """
    Schema for individual chat message
    """
    role: str
    content: str

    class Config:
        schema_extra = {
            "example": {
                "role": "user",
                "content": "What is the weather in Dubai?"
            }
        }

class ChatRequest(BaseModel):
    """
    Schema for chat completion request
    """
    messages: List[Message]
    model: str = "deepseek-chat"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 4096

    class Config:
        schema_extra = {
            "example": {
                "messages": [
                    {"role": "user", "content": "Hello, who are you?"}
                ],
                "model": "deepseek-chat",
                "temperature": 0.7,
                "max_tokens": 4096
            }
        }

class ChatResponse(BaseModel):
    """
    Schema for chat completion response
    """
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[dict]
    usage: dict
