from google.adk.agents import Agent
from agents.prompts.engineering_prompt import ENGINEERING_SYSTEM_PROMPT
from agents.tools.engineering_tools import (
    estimate_api_effort,
    architecture_review,
)
engineering_agent = Agent(
    name="engineering_agent",
    description="Software engineering specialist.",
    instruction=ENGINEERING_SYSTEM_PROMPT,

tools=[
    estimate_api_effort,
    architecture_review,
],
)
