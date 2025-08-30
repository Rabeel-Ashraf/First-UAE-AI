# backend/database/init_db.py
from backend.database.session import engine, Base
from backend.models.user import User
from backend.models.chat_log import ChatLog

def init_db():
    """
    Initialize database tables
    Call this on application startup
    """
    Base.metadata.create_all(bind=engine)

# Optional: Add sample data for development
def create_sample_data():
    """Create sample data for testing"""
    from sqlalchemy.orm import Session
    from backend.database.session import SessionLocal
    from backend.models.user import User
    from backend.core.security import get_password_hash
    
    db: Session = SessionLocal()
    
    # Create admin user if not exists
    admin = db.query(User).filter(User.username == "admin").first()
    if not admin:
        admin = User(
            username="admin",
            hashed_password=get_password_hash("admin123")
        )
        db.add(admin)
        db.commit()
    
    db.close()
