from fastapi import FastAPI

from backend.app.agent import Agent
from backend.app.schemas import AgentRequest, AgentResponse


app = FastAPI(
    title="AgentForge",
    description="AI Agent Evaluation and Automation Platform",
    version="0.1.0",
)


agent = Agent()


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
    return agent.run(request.task)