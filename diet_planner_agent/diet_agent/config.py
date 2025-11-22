import os
from dataclasses import dataclass

# Put your Gemini API key in the environment BEFORE running the agent
# Example (PowerShell):
# $env:GOOGLE_API_KEY="your-key-here"

@dataclass
class AgentConfig:
    worker_model: str = "gemini-2.5-flash"
    critic_model: str = "gemini-2.5-pro"

config = AgentConfig()
