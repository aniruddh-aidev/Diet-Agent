from google.adk.agents import Agent
from google.adk.tools import google_search
from ..config import config
from ..agent_utils import suppress_output_callback

nutrition_analyzer = Agent(
    name="nutrition_analyzer",
    model=config.worker_model,
    description="Checks the nutritional balance of the plan.",
    instruction="""
    Receive the meal plan from session state under 'meal_plan'.
    Provide calories and macro estimates.
    Adjust suggestions if something looks unreasonable.
    Produce a short markdown explanation.
    """,
    tools=[],
    output_key="nutrition_notes",
    after_agent_callback=suppress_output_callback,
)
