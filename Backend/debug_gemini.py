import os
import requests
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

key = os.getenv("GEMINI_API_KEY")

if not key:
    print("GEMINI_API_KEY is missing!")
    exit(1)

url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "gemini-3.6-flash",
    "messages": [
        {"role": "user", "content": "Respond with exactly: GEMINI_API_TEST_SUCCESS"}
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
            print("Success Response:", data["choices"][0]["message"]["content"])
    except Exception as e:
        print("Response Text:", response.text)
except Exception as e:
    print("Exception:", str(e))
