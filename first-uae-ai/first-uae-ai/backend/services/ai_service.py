import httpx
import json
from backend.core.prompts import SYSTEM_PROMPT
from backend.core.config import settings

async def stream_ai_response(request):
    body = await request.body()
    data = json.loads(body)
    messages = data.get("messages", [])
    
    # Inject system prompt
    if not messages or messages[0].get("role") != "system":
        messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
    else:
        messages[0]["content"] = SYSTEM_PROMPT

    async with httpx.AsyncClient(timeout=30.0) as client:
        async with client.stream(
            "POST",
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {settings.deepseek_api_key}"},
            json={**data, "messages": messages}
        ) as resp:
            async for chunk in resp.aiter_bytes():
                text = chunk.decode("utf-8", errors="ignore")
                yield text.replace("DeepSeek", "First UAE AI").replace("deepseek", "First UAE AI")
