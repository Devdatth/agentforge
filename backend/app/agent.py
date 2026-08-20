from typing import Dict
from backend.app.tools.registry import ToolRegistry
from backend.app.tools.selector import ToolSelector


class Agent:
    """
    Core AgentForge agent.

    The agent receives a ToolRegistry so it can
    discover and execute available tools.
    """

    def __init__(
        self,
        name: str = "AgentForge-Agent",
        tool_registry: ToolRegistry | None = None,
    ):
        self.name = name
        self.tool_registry = tool_registry or ToolRegistry()
        self.tool_selector = ToolSelector(self.tool_registry)

    def run(self, task: str) -> Dict:
        """
        Execute an agent task.
        """

        if not task.strip():
            return {
                "success": False,
                "error": "Task cannot be empty",
            }

        return {
            "success": True,
            "agent": self.name,
            "task": task,
            "response": f"Agent received task: {task}",
        }

    def get_available_tools(self) -> list[str]:
        """
        Return the names of tools available to the agent.
        """

        return self.tool_registry.list_tools()

    def run_tool(self, tool_name: str, **kwargs) -> Dict:
        """
        Execute a registered tool by name.
        """

        tool = self.tool_registry.get(tool_name)

        if tool is None:
            return {
                "success": False,
                "error": f"Tool '{tool_name}' not found",
            }

        try:
            result = tool.run(**kwargs)

            return {
                "success": True,
                "tool": tool.name,
                "result": result,
            }

        except Exception as exc:
            return {
                "success": False,
                "tool": tool.name,
                "error": str(exc),
            }
    def run_task(self, task: str) -> Dict:
        """
        Select an appropriate tool for a task, extract parameters,
        and execute it.
        """

        if not task.strip():
            return {
                "success": False,
                "error": "Task cannot be empty",
            }

        tool_name = self.tool_selector.select(task)

        if tool_name is None:
            return {
                "success": False,
                "error": "No suitable tool found",
            }

        kwargs = self._extract_parameters(task, tool_name)

        if kwargs is None:
            kwargs = {}

        result = self.run_tool(tool_name, **kwargs)

        result["task"] = task
        result["selected_tool"] = tool_name

        return result

    def _extract_parameters(self, task: str, tool_name: str) -> Dict:
        """
        Extract tool-specific parameters from a task.
        """

        kwargs = {}

        if tool_name == "calculator":
            expression = task.lower()

            for phrase in [
                "calculate",
                "what is",
                "solve",
                "compute",
            ]:
                expression = expression.replace(phrase, "")

            kwargs["expression"] = expression.strip(" ?")

        elif tool_name == "weather":
            city = task.lower()

            for phrase in [
                "what is the weather in",
                "what's the weather in",
                "what is the weather",
                "what's the weather",
                "weather in",
                "weather",
                "today",
            ]:
                city = city.replace(phrase, "")

            kwargs["city"] = city.strip(" ?").title()

        return kwargs