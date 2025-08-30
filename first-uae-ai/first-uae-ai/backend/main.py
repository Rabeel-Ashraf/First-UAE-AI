from fastapi import FastAPI
from backend.api.routes import auth, chat, admin, whatsapp
from backend.core.config import settings
from backend.database.init_db import init_db
from backend.database.session import engine

app = FastAPI(title="First UAE AI - OrionixLabs", version="1.0")

# Initialize DB
@app.on_event("startup")
def on_startup():
    init_db()

# Include routers
app.include_router(auth.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(whatsapp.router, prefix="")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
