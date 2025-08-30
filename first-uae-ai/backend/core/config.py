from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440
    database_url: str
    redis_url: str
    deepseek_api_key: str
    rate_limit_requests: int = 100
    rate_limit_window: int = 3600
    admin_key: str
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    
    class Config:
        env_file = "../../.env"

settings = Settings()
