from google.adk.agents import Agent, LoopAgent
from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import DietTextValidationChecker

diet_writer_core = Agent(
    name="diet_writer_core",
    model=config.worker_model,
    description="Formats the final diet plan.",
    instruction="""
    Combine the meal plan and nutrition notes into a clean markdown diet document.
    Keep it friendly and practical.
    Do not over-explain.
    """,
    output_key="diet_text",
    after_agent_callback=suppress_output_callback,
)

diet_writer = LoopAgent(
    name="diet_writer",
    description="Retries formatting until valid.",
    sub_agents=[diet_writer_core, DietTextValidationChecker(name="diet_check")],
    max_iterations=3,
)
