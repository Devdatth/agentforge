from pydantic import BaseModel
from typing import Dict, List, Any

class AgentRequest(BaseModel):
    task: str

class TraceStep(BaseModel):
    step: str
    status: str
    details: str

class AgentResponse(BaseModel):
    success: bool
    task: str
    selected_tool: str | None = None
    tool: str | None = None
    result: object | None = None
    error: str | None = None
    trace: List[TraceStep] = []

class ToolRequest(BaseModel):
    tool: str
    arguments: dict = {}

class ToolResponse(BaseModel):
    success: bool
    tool: str | None = None
    result: object | None = None
    error: str | None = None   

     