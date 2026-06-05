import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.ui import Console

from autogen_ext.models.ollama import OllamaChatCompletionClient


# -------------------------
# Ollama model client
# -------------------------
model_client = OllamaChatCompletionClient(
    model="mistral",
    base_url="http://localhost:11434"
)

# -------------------------
# Agents
# -------------------------
bret = AssistantAgent(
    name="Bret",
    model_client=model_client,
    system_message="You are Bret, a stand-up comedian."
)

jemaine = AssistantAgent(
    name="Jemaine",
    model_client=model_client,
    system_message="You are Jemaine, a stand-up comedian."
)

# -------------------------
# Conversation rules
# -------------------------
termination = MaxMessageTermination(6)

# -------------------------
# Team 
# -------------------------
team = RoundRobinGroupChat(
    participants=[bret, jemaine],
    termination_condition=termination
)

# -------------------------
# Run conversation
# -------------------------
async def main():
    await Console(team.run_stream(task="Start a comedy conversation"))

asyncio.run(main())