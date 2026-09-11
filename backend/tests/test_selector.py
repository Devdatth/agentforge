from backend.app.tools.calculator import CalculatorTool
from backend.app.tools.registry import ToolRegistry
from backend.app.tools.selector import ToolSelector
from backend.app.tools.base import BaseTool


class WeatherTool(BaseTool):
    name = "weather"
    description = "Provides weather information."

    capabilities = [
        "weather",
        "temperature",
        "forecast",
    ]

    def run(self, **kwargs):
        return "Sunny"


def create_selector():
    registry = ToolRegistry()
    registry.register(CalculatorTool())

    return ToolSelector(registry)


def test_select_calculator():
    selector = create_selector()

    assert selector.select("Calculate 25 * 48") == "calculator"


def test_select_calculator_with_multiply():
    selector = create_selector()

    assert selector.select("Multiply 10 by 5") == "calculator"


def test_select_calculator_with_division():
    selector = create_selector()

    assert selector.select("Divide 100 by 4") == "calculator"


def test_select_unknown_task():
    selector = create_selector()

    assert selector.select("Tell me about AI agents") is None


def test_select_calculator_with_times():
    selector = create_selector()

    assert selector.select("What is 25 times 48?") == "calculator" 

def test_calculator_capabilities():
    selector = create_selector()

    calculator = selector.registry.get("calculator")

    assert calculator is not None
    assert "multiply" in calculator.capabilities
    assert "divide" in calculator.capabilities

def test_selector_use_tool_capabilities():
    selector = create_selector()

    assert selector.select("what is 25 times 48 ?") == "calculator"
    assert selector.select("Calculate 100 divided by 4") =="calculator"

def test_selector_can_select_weather_tool():
    registry = ToolRegistry()

    registry.register(CalculatorTool())
    registry.register(WeatherTool())

    selector = ToolSelector(registry)

    assert selector.select("What is the weather today?") == "weather"
    assert selector.select("What is the temperature?") == "weather"
    assert selector.select("Give me the forecast") == "weather"    

