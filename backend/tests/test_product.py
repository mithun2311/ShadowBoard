import asyncio

from google.genai.types import Content, Part

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

USER_ID = "mithun"
SESSION_ID = "product_session"


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
ShadowBoard currently has 15 planned features.

Sprint capacity is 5 features per sprint.

A new AI-powered Document Search feature has:

Business Value = 9
Customer Impact = 8
Technical Effort = 4

Please:

1. Prioritize this feature.
2. Estimate the release plan.
3. Explain your reasoning.

Provide your response in the following format:

Executive Summary

Product Analysis

Priority Recommendations

Risks

Next Sprint Plan

Confidence Score (0–100)
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