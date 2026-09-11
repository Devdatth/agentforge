from .base import BaseTool
class WeatherTool(BaseTool):
    name = "weather"
    description = "Provides weather information for a city."

    keywords = [
        "weather",
        "temperature",
        "forecast",
        "rain",
        "sunny",
    ]

    def run(self, city: str):
        return {
            "success": True,
            "tool": "weather",
            "result": f"Weather in {city}: Sunny"
        }