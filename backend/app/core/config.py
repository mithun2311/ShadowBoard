from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    # App
    APP_NAME: str = "ShadowBoard AI"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Auth
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24
    
    # Database
    DATABASE_URL: str
    
    # Redis / Celery
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    # Gemini
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-2.5-pro"
    GEMINI_EMBEDDING_MODEL: str = "text-embedding-004"
    
    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION: str = "shadowboard_documents"
    
    # Lyzr
    LYZR_API_KEY: str
    LYZR_BASE_URL: str = "https://api.lyzr.ai"
    
    # CORS
    CORS_ORIGINS: str = "http://localhost:5173"

settings = Settings()