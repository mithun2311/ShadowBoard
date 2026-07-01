import asyncio

from google.genai.types import Content, Part

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

USER_ID = "mithun"
SESSION_ID = "marketing_session"


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
ShadowBoard AI is launching for software companies.

Marketing Budget = ₹5,00,000

Expected Leads = 2500

Target Audience = Enterprise

Please provide:

1. Marketing Strategy
2. Campaign Analysis
3. Recommended Marketing Channels
4. KPIs
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