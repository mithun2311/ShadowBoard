from google.adk.agents import Agent
from agents.prompts.moderator_prompt import MODERATOR_SYSTEM_PROMPT

from agents.tools.moderator_tools import (
    summarize_votes,
    consensus_score,
)
moderator_agent = Agent(
    name="moderator_agent",
    description="Discussion coordinator.",
    instruction=MODERATOR_SYSTEM_PROMPT,

tools=[
    summarize_votes,
    consensus_score,
],
)