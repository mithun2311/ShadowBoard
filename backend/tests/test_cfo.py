import asyncio

from google.genai.types import Content, Part

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

USER_ID = "mithun"
SESSION_ID = "cfo_session"


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
Estimate the budget for a team of
6 engineers,
salary ₹90,000/month,
duration 8 months.

Also calculate ROI if revenue is ₹75 lakh.
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