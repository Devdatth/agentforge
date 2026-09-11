from pydantic import BaseModel
from typing import Dict, Any
class AgentRequest(BaseModel):
    task: str


class AgentResponse(BaseModel):
    success: bool
    task: str
    selected_tool: str | None = None
    tool: str | None = None
    result: object | None = None
    error: str | None = None

class ToolRequest(BaseModel):
    tool: str
    arguments: dict = {}

class ToolResponse(BaseModel):
    success: bool
    tool: str | None = None
    result: object | None = None
    error: str | None = None    