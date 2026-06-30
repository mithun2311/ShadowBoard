from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup() -> None:
    logger.info(f"{settings.APP_NAME} starting in {settings.ENVIRONMENT} mode")

@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": settings.APP_NAME}

@app.get("/")
async def root() -> dict:
    return {"message": "ShadowBoard AI backend is running. See /docs for API."}