from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import datetime

from .config import config
from .tools import save_diet_to_file, parse_user_prefs
from .sub_agents.meal_planner import meal_planner
from .sub_agents.nutrition_analyzer import nutrition_analyzer
from .sub_agents.diet_writer import diet_writer
from .sub_agents.summary_generator import summary_generator



interactive_diet_agent = Agent(
    name="interactive_diet_agent",
    model=config.worker_model,
    description="Helps users create a simple diet plan.",
    instruction=f"""
    You help users build diet plans.

    Workflow:
    1. Ask for dietary preferences and store them using `parse_user_prefs`.
    2. Generate a meal plan using the meal_planner sub-agent.
    3. Run nutrition analysis using nutrition_analyzer.
    4. Combine everything into a final document using diet_writer.
    5. Optionally create a short summary.
    6. Ask if user wants to save the plan; if yes, call save_diet_to_file.

    Today's date: {datetime.datetime.now().strftime('%Y-%m-%d')}
    """,
    sub_agents=[
        meal_planner,
        nutrition_analyzer,
        diet_writer,
        summary_generator,
    ],
    tools=[
        FunctionTool(save_diet_to_file),
        FunctionTool(parse_user_prefs),
    ],
    output_key="diet_text",
)

root_agent = interactive_diet_agent
