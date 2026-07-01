from google.adk.agents import Agent
from agents.prompts.product_prompt import PRODUCT_SYSTEM_PROMPT
from agents.tools.product_tools import (
    prioritize_feature,
    estimate_release,
)
product_agent = Agent(
    name="product_agent",
    description="Product strategy specialist.",
    instruction=PRODUCT_SYSTEM_PROMPT,

tools=[
    prioritize_feature,
    estimate_release,
],
)
