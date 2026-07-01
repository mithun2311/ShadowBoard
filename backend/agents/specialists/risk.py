from google.adk.agents import Agent
from agents.tools.risk_tools import (
    assess_risk,
    mitigation_plan,
)
from agents.prompts.risk_prompt import RISK_SYSTEM_PROMPT
from agents.tools.qdrant_tools import search_documents

risk_agent = Agent(
    name="risk_agent",
    model="gemini-2.5-flash",
    description="Enterprise risk assessment specialist.",
    instruction=RISK_SYSTEM_PROMPT,
    
tools=[
    assess_risk,
    mitigation_plan,
    search_documents,
],
)
