import asyncio

from google.genai.types import Content, Part

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

USER_ID = "mithun"
SESSION_ID = "engineering_session"


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
                text="""
We are building an AI SaaS platform using:

- FastAPI
- React
- PostgreSQL
- Redis
- Qdrant

Please review this architecture and estimate the engineering effort
for implementing 18 REST API endpoints with HIGH complexity.

Provide your response in the following format:

1. Executive Summary
2. Technical Analysis
3. Risks
4. Recommendations
5. Confidence Score
"""
            )
        ],
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(event.content.parts[0].text)
            else:
                print("No response received from the model.")


if __name__ == "__main__":
    asyncio.run(main())