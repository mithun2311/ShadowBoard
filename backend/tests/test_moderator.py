import asyncio

from google.genai.types import Content, Part

from agents.runtime import (
    runner,
    session_service,
    APP_NAME,
)

USER_ID = "mithun"
SESSION_ID = "moderator_session"


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
The executive team has provided the following opinions:

CFO:
Proceed with the project.

Engineering:
Proceed after performance optimization.

Legal:
Proceed after adding a privacy policy.

Marketing:
Launch with an early access program.

Risk:
Proceed after cybersecurity review.

Please moderate this executive discussion.

Provide:

Executive Summary

Executive Opinions

Consensus

Trade-offs

Final Recommendation

Confidence Score
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
                print("No response received.")


if __name__ == "__main__":
    asyncio.run(main())