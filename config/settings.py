from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

# Example: Together AI endpoint (change if using OpenRouter or others)
API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"

SYSTEM_PROMPT = (
    "You are DeepSeek Chat, an AI assistant. "
    "Answer queries in a helpful, clear, and concise manner. "
    "Today’s date is {current_date}."
)
