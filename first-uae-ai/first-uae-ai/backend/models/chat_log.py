from sqlalchemy import Column, String, Text, DateTime, func
from backend.database.session import Base

class ChatLog(Base):
    __tablename__ = "chat_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    prompt = Column(Text)
    response = Column(Text)
    created_at = Column(DateTime, default=func.now())
