from google.adk.agents import Agent
from agents.tools.risk_tools import (
    assess_risk,
    mitigation_plan,
)
from agents.prompts.risk_prompt import RISK_SYSTEM_PROMPT

risk_agent = Agent(
    name="risk_agent",
    model="gemini-2.5-flash",
    description="Enterprise risk assessment specialist.",
    instruction=RISK_SYSTEM_PROMPT,
    
tools=[
    assess_risk,
    mitigation_plan,
],
)
