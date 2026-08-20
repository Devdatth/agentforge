class WeatherTool(BaseTool):
    name = "weather"
    description = "Provides weather information for a city."

    def run(self, city: str):
        return {
            "success": True,
            "tool": "weather",
            "result": f"Weather in {city}: Sunny"
        }