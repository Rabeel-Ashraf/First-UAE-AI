# backend/schemas/user.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    """
    Schema for user registration
    """
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "firstuaeai",
                "password": "securepassword123"
            }
        }

class Token(BaseModel):
    """
    Schema for JWT authentication response
    """
    access_token: str
    token_type: str

    class Config:
        schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xJ...",
                "token_type": "bearer"
            }
        }

class UserOut(BaseModel):
    """
    Schema for user response (without password)
    """
    username: str

    class Config:
        orm_mode = True
