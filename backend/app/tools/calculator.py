from .base import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Performs basic mathematical calculations."

    def run(self, expression: str):
        try:
            return eval(expression, {"__builtins__": {}}, {})
        except Exception:
            return None