import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

key = os.getenv("GROK_API_KEY")

if not key:
    print("GROK_API_KEY is missing!")
    exit(1)

url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "grok-2",
    "messages": [
        {"role": "system", "content": "You are a test assistant."},
        {"role": "user", "content": "Hello"}
    ]
}

try:
    response = requests.post(url, json=payload, headers=headers)
    print("HTTP Status:", response.status_code)
    try:
        data = response.json()
        if "error" in data:
            print("Provider Error:", data["error"])
        else:
            print("Success Response.")
    except Exception as e:
        print("Response Text:", response.text)
except Exception as e:
    print("Exception:", str(e))
