from fastapi import APIRouter, Request, Form
from twilio.twiml.messaging_response import MessagingResponse
from backend.services.ai_service import get_ai_response_sync

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(
    From: str = Form(None),
    Body: str = Form("")
):
    reply_text = get_ai_response_sync(Body) or "I'm offline. Try later."
    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp)
