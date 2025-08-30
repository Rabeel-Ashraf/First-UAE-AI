# backend/main.py
from fastapi import FastAPI
from backend.api.routes import auth, chat, admin, whatsapp
from backend.core.config import settings
from backend.database.init_db import init_db
from backend.database.session import engine

app = FastAPI(
    title="First UAE AI - OrionixLabs",
    version="1.0",
    description="Dubai's first branded AI assistant, developed by OrionixLabs.com"
)

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    init_db()

# Include API routers
app.include_router(auth.router, prefix="/api", tags=["Authentication"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(admin.router, prefix="/api", tags=["Admin"])
app.include_router(whatsapp.router, tags=["WhatsApp"])

# Root health check
@app.get("/")
def health():
    return {
        "status": "alive",
        "service": "First UAE AI",
        "region": "Dubai",
        "developer": "OrionixLabs.com"
    }

# Run with: uvicorn backend.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
