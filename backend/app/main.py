from fastapi import FastAPI

app = FastAPI(
    title="AgentForge",
    description="AI Agent Evaluation and Automation Platform",
    version="0.1.0",
)


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