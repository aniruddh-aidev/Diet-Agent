from google.adk.agents import Agent
from ..config import config
from ..agent_utils import suppress_output_callback

summary_generator = Agent(
    name="summary_generator",
    model=config.worker_model,
    description="Creates a short summary of the diet plan.",
    instruction="""
    Generate a brief summary (3–5 sentences) highlighting:
    - Goal of the diet
    - What the plan includes
    - Key nutritional considerations
    Output in plain text.
    """,
    output_key="diet_summary",
    after_agent_callback=suppress_output_callback,
)
