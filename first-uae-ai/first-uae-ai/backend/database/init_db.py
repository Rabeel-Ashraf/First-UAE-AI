from backend.database.session import engine, Base
from backend.models.user import User
from backend.models.chat_log import ChatLog

def init_db():
    Base.metadata.create_all(bind=engine)
