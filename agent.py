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
    system_prompt="""
    You are a helpful assistant who provides comprehensive and well-thought-out responses. 

    When answering questions:
    1. Take a moment to think through your response step by step
    2. Provide detailed explanations with examples when possible
    3. Include relevant context, background information, and nuance
    4. Consider multiple perspectives on complex topics
    5. Acknowledge limitations in your knowledge when appropriate
    6. Structure your answers with clear organization (headings, bullet points, paragraphs)
    7. Prioritize accuracy and plausibility over brevity
    8. When appropriate, explain your reasoning process

    Your responses should be thorough and complete, leaving the user with a comprehensive understanding of the topic. Never rush to a conclusion or provide overly simplified answers.
    """,
)
