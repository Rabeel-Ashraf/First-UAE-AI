# tests/integration/test_whatsapp.py
from fastapi.testclient import TestClient
from backend.main import app
from fastapi import Form
from unittest.mock import AsyncMock, patch

client = TestClient(app)

# Mock Twilio request data
MOCK_FROM = "whatsapp:+1234567890"
MOCK_BODY = "Hello, who are you?"

def test_whatsapp_webhook_returns_twiml():
    """
    Test that WhatsApp webhook returns valid TwiML response
    """
    response = client.post(
        "/whatsapp",
        data={
            "From": MOCK_FROM,
            "Body": MOCK_BODY
        }
    )

    assert response.status_code == 200
    assert "text/xml" in response.headers["content-type"]
    assert "<Response>" in response.text
    assert "<Message>" in response.text

def test_whatsapp_response_contains_ai_reply():
    """
    Test that the AI responds and the message is included
    """
    with patch("backend.services.ai_service.get_ai_response_sync") as mock_ai:
        mock_ai.return_value = "I am First UAE AI, developed by OrionixLabs in Dubai."

        response = client.post(
            "/whatsapp",
            data={
                "From": MOCK_FROM,
                "Body": "Who made you?"
            }
        )

        assert response.status_code == 200
        assert "First UAE AI" in response.text
        assert "OrionixLabs" in response.text
        assert "DeepSeek" not in response.text  # 🔐 No model leak

def test_whatsapp_empty_message():
    """
    Test behavior when message body is empty or missing
    """
    response = client.post(
        "/whatsapp",
        data={
            "From": MOCK_FROM,
            "Body": ""
        }
    )

    assert response.status_code == 200
    assert "مرحباً!" in response.text or "Hello" in response.text  # Welcome message

def test_whatsapp_arabic_input():
    """
    Test that WhatsApp handles Arabic input correctly
    """
    with patch("backend.services.ai_service.get_ai_response_sync") as mock_ai:
        mock_ai.return_value = "نعم، يمكنني التحدث بالعربية. كيف يمكنني مساعدتك؟"

        response = client.post(
            "/whatsapp",
            data={
                "From": "whatsapp:+971501234567",
                "Body": "هل يمكنك التحدث بالعربية؟"
            }
        )

        assert response.status_code == 200
        assert "العربية" in response.text
