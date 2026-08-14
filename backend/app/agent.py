from typing import Dict

from backend.app.tools.registry import ToolRegistry


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