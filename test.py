import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY") or "your_api_key_here"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # required by OpenRouter
    "X-Title": "Local Test",             # required by OpenRouter
}

data = {
    "model": "deepseek/deepseek-chat-v3-0324:free",  # ✅ Correct model
    "messages": [
        {"role": "user", "content": "Hello DeepSeek, testing via requests!"}
    ]
}

response = requests.post(API_URL, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)

if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("\nBot Reply:", reply)
