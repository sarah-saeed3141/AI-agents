import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.ollama import OllamaChatCompletionClient

model_client = OllamaChatCompletionClient(
    model="mistral",
    base_url="http://localhost:11434"
)

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

async def run():
    result = await bret.run(task="Tell a joke to Jemaine")
    print(result)

asyncio.run(run())