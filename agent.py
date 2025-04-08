import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

load_dotenv()

model = OpenAIModel(
    "openrouter/quasar-alpha",
    provider=OpenAIProvider(
        base_url=os.getenv("OPENROUTER_BASE_URL"),
        api_key=os.getenv("OPENROUTER_API_KEY"),
    ),
)
agent = Agent(
    model,
    system_prompt="You are a helpful assistant. Only speak in short riddles.",
)
