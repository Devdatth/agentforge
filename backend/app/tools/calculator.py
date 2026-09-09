from .base import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Performs basic mathematical calculations."

    capabilities = [
        "calculate",
        "calculator",
        "math",
        "multiply",
        "divide",
        "subtract",
        "subtraction",
        "times",
        "minus",
    ]
    keywords = [
        "calculate",
        "calculator",
        "add",
        "addition",
        "subtract",
        "minus",
        "multiply",
        "times",
        "divide",
    ]

    def run(self, expression: str):
        try:
            return eval(expression, {"__builtins__": {}}, {})
        except Exception:
            return None