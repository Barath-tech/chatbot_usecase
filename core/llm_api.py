import os
import requests
from config.settings import API_URL, MODEL_NAME

def send_to_llm(messages, model=MODEL_NAME):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",   # required by OpenRouter
        "X-Title": "Streamlit Chatbot",       # required by OpenRouter
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("🔎 Status:", response.status_code)
        print("🔎 Raw Response:", response.text)

        # Try parsing JSON
        data = response.json()

        # If API returned an error, handle gracefully
        if "error" in data:
            error_msg = data["error"].get("message", "Unknown error")

            # Auto fallback if DeepSeek is overloaded
            if "rate-limited" in error_msg.lower():
                fallback_model = "mistralai/mistral-7b-instruct:free"
                print(f"⚠️ DeepSeek busy. Switching to fallback model: {fallback_model}")
                payload["model"] = fallback_model
                fb_response = requests.post(API_URL, headers=headers, json=payload)
                try:
                    return fb_response.json()
                except Exception:
                    return {
                        "choices": [
                            {"message": {"content": f"⚠️ Fallback also failed: {fb_response.text}"}}
                        ]
                    }

            return {
                "choices": [
                    {"message": {"content": f"⚠️ API Error: {error_msg}"}}
                ]
            }

        return data

    except Exception as e:
        return {
            "choices": [
                {"message": {"content": f"❌ Request failed: {str(e)}"}}
            ]
        }
