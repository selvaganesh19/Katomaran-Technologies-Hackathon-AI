from langchain.chat_models import ChatOpenAI
import os

# Load OpenRouter credentials
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
    model_name=os.getenv("OPENROUTER_MODEL"),  # e.g. "openrouter/gpt-4"
    temperature=0,
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)
