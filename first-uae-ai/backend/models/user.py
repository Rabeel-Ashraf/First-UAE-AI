# backend/models/user.py
from sqlalchemy import Column, Integer, String
from backend.database.session import Base

class User(Base):
    """
    User model for authentication and authorization
    Stores username and hashed password
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}')>"
