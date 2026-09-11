from fastapi import FastAPI

from backend.app.agent import Agent
from backend.app.schemas import (
    AgentRequest,
    AgentResponse,
    ToolRequest,
    ToolResponse,
)
from backend.app.tools.calculator import CalculatorTool
from backend.app.tools.registry import ToolRegistry

app = FastAPI(
    title="AgentForge",
    description="AI Agent Evaluation and Automation Platform",
    version="0.1.0",
)


tool_registry = ToolRegistry()
tool_registry.register(CalculatorTool())

agent = Agent(tool_registry=tool_registry)


@app.get("/")
def root():
    return {
        "project": "AgentForge",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/agent/run", response_model=AgentResponse)
def run_agent(request: AgentRequest):
    return agent.run_task(request.task)


@app.post("/agent/tool", response_model=ToolResponse)
def run_tool(request: ToolRequest):
    return agent.run_tool(
        request.tool,
        **request.arguments,
    )