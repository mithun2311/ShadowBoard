from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # ------------------------
    # Application
    # ------------------------
    APP_NAME: str = "ShadowBoard AI"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # ------------------------
    # Authentication
    # ------------------------
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 1440

    # ------------------------
    # Database
    # ------------------------
    DATABASE_URL: str

    # ------------------------
    # Redis
    # ------------------------
    REDIS_URL: str

    CELERY_BROKER_URL: str | None = None
    CELERY_RESULT_BACKEND: str | None = None

    # ------------------------
    # Gemini
    # ------------------------
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-2.5-flash"
    GEMINI_EMBEDDING_MODEL: str = "gemini-embedding-001"

    # ------------------------
    # Qdrant
    # ------------------------
    QDRANT_URL: str
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION: str = "shadowboard_documents"

    # ------------------------
    # Lyzr
    # ------------------------
    LYZR_API_KEY: str
    LYZR_BASE_URL: str = "https://agent-prod.studio.lyzr.ai"

    # ------------------------
    # CORS
    # ------------------------
    CORS_ORIGINS: str


settings = Settings()
