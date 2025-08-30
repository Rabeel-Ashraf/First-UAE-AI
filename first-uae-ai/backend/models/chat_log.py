# backend/models/chat_log.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from backend.database.session import Base

class ChatLog(Base):
    """
    ChatLog model for storing conversation history
    Used for auditing, analytics, and compliance
    """
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)  # username
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    model = Column(String, default="deepseek-chat")
    created_at = Column(DateTime, default=func.now(), nullable=False)

    def __repr__(self):
        return f"<ChatLog(user='{self.user_id}', created_at='{self.created_at}')>"
