from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["project"] == "AgentForge"


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

#Second part
def test_agent_run():
    response = client.post(
        "/agent/run",
        json={
            "task": "Calculate 10+5"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["task"] == "Calculate 10+5"
    assert data["selected_tool"] == "calculator"


def test_agent_empty_task():
    response = client.post(
        "/agent/run",
        json={
            "task": ""
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["error"] == "Task cannot be empty"

def test_agent_tool_endpoint():
    response = client.post(
        "/agent/tool",
        json={
            "tool": "calculator",
            "arguments": {
                "expression": "25 * 48"
            },
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["tool"] == "calculator"
    assert data["result"] == 1200


def test_agent_tool_unknown_tool():
    response = client.post(
        "/agent/tool",
        json={
            "tool": "unknown",
            "arguments": {},
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["error"] == "Tool 'unknown' not found"   