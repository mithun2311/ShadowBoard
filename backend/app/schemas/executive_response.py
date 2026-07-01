from pydantic import BaseModel


class ExecutiveResponse(BaseModel):
    agent: str
    executive_summary: str
    detailed_analysis: str
    risks: list[str]
    recommendations: list[str]
    confidence_score: int