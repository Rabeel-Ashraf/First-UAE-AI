# backend/services/ai_service.py
import httpx
import json
from typing import AsyncGenerator
from backend.core.config import settings
from backend.core.prompts import SYSTEM_PROMPT

async def stream_ai_response(request) -> AsyncGenerator[bytes, None]:
    """
    Stream AI response from DeepSeek API with branding protection
    Handles prompt injection, response streaming, and model identity sanitization
    """
    # Parse incoming request
    body = await request.body()
    data = json.loads(body)
    messages = data.get("messages", [])
    
    # Inject system prompt to maintain brand identity
    if not messages or messages[0].get("role") != "system":
        messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
    else:
        messages[0]["content"] = SYSTEM_PROMPT

    # Call DeepSeek API
    async with httpx.AsyncClient(timeout=30.0) as client:
        headers = {
            "Authorization": f"Bearer {settings.deepseek_api_key}",
            "Content-Type": "application/json"
        }
        
        async with client.stream(
            "POST",
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json={**data, "messages": messages}
        ) as response:
            async for chunk in response.aiter_bytes():
                # Sanitize response to protect brand identity
                text = chunk.decode("utf-8", errors="ignore")
                text = text.replace("DeepSeek", "First UAE AI").replace("deepseek", "First UAE AI")
                yield text.encode("utf-8")

def get_ai_response_sync(prompt: str) -> str:
    """
    Synchronous version for WhatsApp integration
    Returns cleaned AI response
    """
    import httpx
    import json
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]
    
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {settings.deepseek_api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": messages,
                    "temperature": 0.7
                }
            )
            response.raise_for_status()
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            # Sanitize response
            return reply.replace("DeepSeek", "First UAE AI").replace("deepseek", "First UAE AI")
    except Exception as e:
        return "I'm currently unavailable. Please try again later."
