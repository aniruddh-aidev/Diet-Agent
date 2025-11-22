import pytest
from diet_agent.agent import root_agent

@pytest.mark.asyncio
async def test_agent_runs():
    response = await root_agent.run_async("Create a diet for testing.")
    assert response is not None
