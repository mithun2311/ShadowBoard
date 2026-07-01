from google.adk.agents import Agent
from agents.prompts.marketing_prompt import MARKETING_SYSTEM_PROMPT
from agents.tools.marketing_tools import (
    estimate_campaign,
    recommend_channel,
)
marketing_agent = Agent(
    name="marketing_agent",
    model="gemini-2.5-flash",
    description="Marketing strategy and growth specialist.",

    instruction=MARKETING_SYSTEM_PROMPT,

tools=[
    estimate_campaign,
    recommend_channel,
],
)
