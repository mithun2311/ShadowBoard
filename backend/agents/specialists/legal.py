from google.adk.agents import Agent
from agents.prompts.legal_prompt import LEGAL_SYSTEM_PROMPT

from agents.tools.legal_tools import (
    assess_compliance,
    identify_legal_risk,
)
legal_agent = Agent(
    name="legal_agent",
    description="Legal and compliance specialist.",
    instruction=LEGAL_SYSTEM_PROMPT,

tools=[
    assess_compliance,
    identify_legal_risk,
],
)