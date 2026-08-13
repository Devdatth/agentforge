from typing import Dict


class Agent:
    """
    Core AgentForge agent.

    This first version provides the basic execution layer.
    Later, this class will handle LLMs, tools, memory, RAG,
    evaluation, and observability.
    """

    def __init__(self, name: str = "AgentForge-Agent"):
        self.name = name

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