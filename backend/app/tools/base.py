from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str
    description: str
    capabilities: list[str] = []

    @abstractmethod
    def run(self, **kwargs):
        pass