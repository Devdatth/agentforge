from backend.app.agent import Agent
from backend.app.tools.calculator import CalculatorTool
from backend.app.tools.registry import ToolRegistry
from backend.app.tools.selector import ToolSelector
from backend.tests.test_selector import WeatherTool


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

def test_agent_selects_calculator():
    result = agent.run_task("Calculate 25 * 48")

    assert result["success"] is True
    assert result["selected_tool"] == "calculator"


def test_agent_handles_unknown_task():
    result = agent.run_task("Tell me about artificial intelligence")

    assert result["success"] is False
    assert result["error"] == "No suitable tool found"  

def test_weather_tool_runs():
    registry = ToolRegistry()

    registry.register(WeatherTool())

    result = registry.get("weather").run(city="Pune")

    assert isinstance(result, str)
    assert result == "Sunny"

def test_agent_runs_weather_task():
    registry = ToolRegistry()

    registry.register(CalculatorTool())
    registry.register(WeatherTool())
    agent = Agent(tool_registry=registry)

    result = agent.run_task("What is the weather in Pune?")

    assert result["success"] is True
    assert result["selected_tool"] == "weather"
    assert "Pune" in result["task"]

def test_agent_extracts_calculator_parameters():
    agent = Agent()

    result = agent._extract_parameters(
        "Solve 10 + 5",
        "calculator",
    )

    assert result == {
        "expression": "10 + 5"
    }   

def test_agent_extracts_weather_parameters():
    agent = Agent()

    result = agent._extract_parameters(
        "What's the weather in Mumbai?",
        "weather",
    )

    assert result == {
        "city": "Mumbai"
    }   

def test_agent_extracts_no_parameters_for_unknown_tool():
    agent = Agent()

    result = agent._extract_parameters(
        "Do something",
        "unknown_tool",
    )

    assert result == {}   

def test_agent_extracts_empty_weather_city():
    agent = Agent()

    result = agent._extract_parameters(
        "What is the weather today?",
        "weather",
    )

    assert result == {
        "city": ""
    }           

def test_agent_execution_trace():
    agent = Agent()

    result = agent.run_task("Calculate 10+5")

    assert result["success"] is True
    assert "trace" in result

    trace = result["trace"]

    assert len(trace) == 3

    # Tool selection trace
    assert trace[0]["step"] == "tool_selection"
    assert trace[0]["status"] == "success"
    assert trace[0]["tool"] == "calculator"

    # Parameter extraction trace
    assert trace[1]["step"] == "parameter_extraction"
    assert trace[1]["status"] == "success"
    assert trace[1]["parameters"] == {
        "expression": "10+5"
    }

    # Tool execution trace
    assert trace[2]["step"] == "tool_execution"
    assert trace[2]["status"] == "success"
    assert trace[2]["tool"] == "calculator"
    assert trace[2]["result"] == 15

def test_agent_execution_steps():
    agent = Agent()

    result = agent.run_task("Calculate 10+5")

    assert result["success"] is True
    assert "execution_steps" in result

    steps = result["execution_steps"]

    assert len(steps) == 1

    step = steps[0]

    assert step["step_number"] == 1
    assert step["tool"] == "calculator"
    assert step["parameters"] == {
        "expression": "10+5"
    }
    assert step["status"] == "success"
    assert step["result"] == 15

def test_agent_multi_step_task():
    agent = Agent()

    result = agent.run_multi_step_task(
        "Calculate 10+5 and tell me the weather in Pune"
    )

    assert result["success"] is True
    assert result["task"] == "Calculate 10+5 and tell me the weather in Pune"

    steps = result["execution_steps"]

    assert len(steps) == 2

    # Step 1: Calculator
    assert steps[0]["step_number"] == 1
    assert steps[0]["tool"] == "calculator"
    assert steps[0]["parameters"] == {
        "expression": "10+5"
    }
    assert steps[0]["status"] == "success"
    assert steps[0]["result"] == 15

    # Step 2: Weather
    assert steps[1]["step_number"] == 2
    assert steps[1]["tool"] == "weather"
    assert steps[1]["parameters"] == {
        "city": "Pune"
    }
    assert steps[1]["status"] == "success"

def test_agent_multi_step_task_stops_on_failure():
    agent = Agent()

    result = agent.run_multi_step_task(
        "Calculate 10+5 and do something impossible"
    )

    assert result["success"] is False
    assert result["task"] == "Calculate 10+5 and do something impossible"

    steps = result["execution_steps"]

    assert len(steps) == 2

    # First step succeeds
    assert steps[0]["step_number"] == 1
    assert steps[0]["tool"] == "calculator"
    assert steps[0]["status"] == "success"
    assert steps[0]["result"] == 15

    # Second step fails because no suitable tool exists
    assert steps[1]["step_number"] == 2
    assert steps[1]["tool"] is None
    assert steps[1]["status"] == "failed"   

def test_run_task_automatically_handles_multi_step_task():
    agent = Agent()

    result = agent.run_task(
        "Calculate 10+5 and tell me the weather in Pune"
    )

    assert result["success"] is True
    assert result["task"] == "Calculate 10+5 and tell me the weather in Pune"

    assert len(result["execution_steps"]) == 2

    assert result["execution_steps"][0]["tool"] == "calculator"
    assert result["execution_steps"][0]["result"] == 15

    assert result["execution_steps"][1]["tool"] == "weather"
    assert result["execution_steps"][1]["parameters"] == {
        "city": "Pune"
    }