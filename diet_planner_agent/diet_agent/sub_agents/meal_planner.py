from google.adk.agents import Agent
from google.adk.tools import google_search
from ..config import config
from ..agent_utils import suppress_output_callback

meal_planner = Agent(
    name="meal_planner",
    model=config.worker_model,
    description="Creates a basic meal plan for the user.",
    instruction="""
    You generate a simple daily diet structure based on user preferences.
    Include breakfast, lunch, dinner, and one snack.
    Keep the plan realistic and balanced.
    Use Google Search when necessary to check basic nutrition facts.
    Format output as markdown.
    """,
    tools=[],
    output_key="meal_plan",
    after_agent_callback=suppress_output_callback,
)
