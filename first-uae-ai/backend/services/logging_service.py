# backend/services/logging_service.py
from sqlalchemy.orm import Session
from backend.models.chat_log import ChatLog
from datetime import datetime

def log_chat(db: Session, user_id: str, prompt: str, response: str, model: str = "deepseek-chat"):
    """
    Log chat interaction to database for auditing and analytics
    """
    chat_log = ChatLog(
        user_id=user_id,
        prompt=prompt[:1000],  # Truncate long prompts
        response=response[:4000],  # Truncate long responses
        model=model,
        created_at=datetime.utcnow()
    )
    try:
        db.add(chat_log)
        db.commit()
        db.refresh(chat_log)
    except Exception as e:
        db.rollback()
        print(f"Logging error: {e}")

def get_chat_logs(db: Session, limit: int = 100):
    """
    Retrieve chat logs for admin panel
    """
    return db.query(ChatLog).order_by(ChatLog.created_at.desc()).limit(limit).all()
