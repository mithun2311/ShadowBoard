import uuid

from fastapi import APIRouter
from google.genai import types

from app.schemas.ai import (
    AIQueryRequest,
    AIQueryResponse,
)

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post(
    "/query",
    response_model=AIQueryResponse,
)
async def query_ai(request: AIQueryRequest):

    user_id = "demo-user"

    session_id = str(uuid.uuid4())

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
    )

    final_text = ""

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=types.Content(
            role="user",
            parts=[
                types.Part(text=request.query),
            ],
        ),
    ):

        if (
            event.content
            and event.content.parts
            and event.content.parts[0].text
        ):
            final_text = event.content.parts[0].text

    return AIQueryResponse(
        response=final_text,
    )