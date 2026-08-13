from pydantic import BaseModel


class AgentRequest(BaseModel):
    task: str


class AgentResponse(BaseModel):
    success: bool
    agent: str | None = None
    task: str | None = None
    response: str | None = None
    error: str | None = None