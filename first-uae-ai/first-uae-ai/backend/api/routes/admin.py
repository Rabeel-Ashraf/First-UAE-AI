from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.config import settings
from backend.database.session import get_db
from backend.models.chat_log import ChatLog

router = APIRouter()

@router.get("/admin/logs")
async def get_logs(request: Request, db: Session = Depends(get_db)):
    if request.headers.get("X-Admin-Key") != settings.ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Invalid admin key")
    logs = db.query(ChatLog).order_by(ChatLog.created_at.desc()).limit(100).all()
    return [{"user": log.user_id, "prompt": log.prompt, "response": log.response, "time": log.created_at} for log in logs]
