from google.adk.agents import Agent

from agents.prompts.cfo_prompt import CFO_SYSTEM_PROMPT

from agents.tools.finance_tools import (
    calculate_roi,
    estimate_budget,
    cost_breakdown,
)
cfo_agent = Agent(
    name="cfo_agent",
    description="Financial analysis specialist.",
    instruction=CFO_SYSTEM_PROMPT,

tools=[
    calculate_roi,
    estimate_budget,
    cost_breakdown,
],
)