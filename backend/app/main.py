from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from app.core.config import settings
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.projects import router as projects_router
from app.api.routes.documents import router as documents_router
from app.api.routes.ai import router as ai_router
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

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(projects_router)
app.include_router(documents_router)
app.include_router(ai_router)
@app.on_event("startup")
async def on_startup() -> None:
    logger.info(f"{settings.APP_NAME} starting in {settings.ENVIRONMENT} mode")

@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": settings.APP_NAME}

@app.get("/")
async def root() -> dict:
    return {"message": "ShadowBoard AI backend is running. See /docs for API."}