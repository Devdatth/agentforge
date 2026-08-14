from backend.app.main import agent
from backend.app.tools.calculator import CalculatorTool
from backend.app.tools.registry import ToolRegistry


def test_register_and_get_tool():
    registry = ToolRegistry()
    calculator = CalculatorTool()

    registry.register(calculator)

    assert registry.get("calculator") is calculator


def test_list_tools():
    registry = ToolRegistry()

    registry.register(CalculatorTool())

    assert registry.list_tools() == ["calculator"]


def test_unknown_tool():
    registry = ToolRegistry()

    assert registry.get("unknown") is None

from backend.app.main import agent

#second part for tool execution 

def test_agent_run_calculator():
    result = agent.run_tool(
        "calculator",
        expression="25 * 48",
    )

    assert result["success"] is True
    assert result["tool"] == "calculator"
    assert result["result"] == 1200


def test_agent_run_unknown_tool():
    result = agent.run_tool("unknown")

    assert result["success"] is False
    assert result["error"] == "Tool 'unknown' not found"    