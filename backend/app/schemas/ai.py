from pydantic import BaseModel


class AIQueryRequest(BaseModel):
    query: str


class AIQueryResponse(BaseModel):
    response: str