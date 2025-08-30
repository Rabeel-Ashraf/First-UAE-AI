from fastapi import APIRouter, Request, Depends
from fastapi.responses import StreamingResponse
from backend.core.security import get_current_user
from backend.services.ai_service import stream_ai_response

router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completion(request: Request, user = Depends(get_current_user)):
    return StreamingResponse(stream_ai_response(request), media_type="text/plain")
