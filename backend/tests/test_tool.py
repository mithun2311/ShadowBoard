import asyncio

from google.genai.types import Content, Part

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

USER_ID = "mithun"
SESSION_ID = "tool_session"


async def main():

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    message = Content(
        role="user",
        parts=[
            Part(
                text="What version of ShadowBoard are you running?"
            )
        ],
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message,
    ):
        if event.is_final_response():
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())