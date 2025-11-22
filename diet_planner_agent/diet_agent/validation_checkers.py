from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions

class PlanValidationChecker(BaseAgent):
    async def _run_async_impl(self, context: InvocationContext):
        if context.session.state.get("meal_plan"):
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name)

class DietTextValidationChecker(BaseAgent):
    async def _run_async_impl(self, context: InvocationContext):
        if context.session.state.get("diet_text"):
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name)
