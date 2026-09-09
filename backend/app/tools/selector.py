from .registry import ToolRegistry


class ToolSelector:
    """
    Selects the most appropriate registered tool for a task.
    """

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def select(self, task: str) -> str | None:
        """
        Select a tool based on the capabilities and keywords
        registered by each tool.
        """

        task_lower = task.lower()

        for tool_name in self.registry.list_tools():
            tool = self.registry.get(tool_name)

            if tool is None:
                continue

            capabilities = getattr(tool, "capabilities", [])
            keywords = getattr(tool, "keywords", [])

            if any(
                capability.lower() in task_lower
                for capability in capabilities
            ):
                return tool_name

            if any(
                keyword.lower() in task_lower
                for keyword in keywords
            ):
                return tool_name

        return None