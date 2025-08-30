from backend.database.session import SessionLocal
from backend.models.chat_log import ChatLog

def log_chat(user_id: str, prompt: str, response: str):
    db = SessionLocal()
    log = ChatLog(user_id=user_id, prompt=prompt, response=response)
    db.add(log)
    db.commit()
    db.close()
