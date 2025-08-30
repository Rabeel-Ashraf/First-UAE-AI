# tests/unit/test_auth.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.core.security import create_access_token
from backend.database.init_db import init_db
from backend.database.session import engine, SessionLocal
from backend.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create test client
client = TestClient(app)

# Setup test DB
@pytest.fixture(scope="module")
def setup_db():
    init_db()
    db = SessionLocal()
    yield db
    db.close()

def test_register_and_login(setup_db):
    # Clean up if test user exists
    db = SessionLocal()
    existing_user = db.query(User).filter(User.username == "testuser").first()
    if existing_user:
        db.delete(existing_user)
        db.commit()
    db.close()

    # Test registration
    reg_response = client.post(
        "/api/register",
        json={"username": "testuser", "password": "testpass123"}
    )
    assert reg_response.status_code == 200
    assert "access_token" in reg_response.json()

    # Test login
    login_response = client.post(
        "/api/token",
        data={"username": "testuser", "password": "testpass123"}
    )
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

def test_invalid_login():
    response = client.post(
        "/api/token",
        data={"username": "wrong", "password": "wrong"}
    )
    assert response.status_code == 400
    assert "Invalid credentials" in response.json()["detail"]
