from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    description: str | None = None
    industry: str | None = None
    company_stage: str | None = None
    decision_type: str | None = None


class ProjectUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    industry: str | None = None
    company_stage: str | None = None
    decision_type: str | None = None
    status: str | None = None


class ProjectResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    industry: str | None
    company_stage: str | None
    decision_type: str | None
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }