class ToolSelector:
    def __init__(self, registry):
        self.registry = registry

    def select(self, task: str):
        task_lower = task.lower()

        for tool_name in self.registry.list_tools():
            tool = self.registry.get(tool_name)

            if not tool:
                continue

            # Check keywords
            keywords = getattr(tool, "keywords", [])

            for keyword in keywords:
                if keyword.lower() in task_lower:
                    return tool_name

            # Check capabilities
            capabilities = getattr(tool, "capabilities", [])

            for capability in capabilities:
                if capability.lower() in task_lower:
                    return tool_name

        # Detect mathematical expressions
        math_operators = ["+", "-", "*", "/", "**"]

        if (
            any(operator in task for operator in math_operators)
            and any(char.isdigit() for char in task)
        ):
            if self.registry.get("calculator"):
                return "calculator"

        return None