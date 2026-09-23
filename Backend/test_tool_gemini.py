import requests
import json
from app.core.config import GEMINI_API_KEY
from app.tools.database_tools import TOOL_DEFINITIONS

url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
headers = {
    "Authorization": f"Bearer {GEMINI_API_KEY}",
    "Content-Type": "application/json"
}

# Simulate first call
messages = [
    {"role": "user", "content": "Find me a hotel in Bengaluru"}
]
payload = {
    "model": "gemini-3.6-flash",
    "messages": messages,
    "tools": TOOL_DEFINITIONS,
    "tool_choice": "auto"
}
response = requests.post(url, json=payload, headers=headers).json()
msg1 = response["choices"][0]["message"]
print("First response:", json.dumps(msg1, indent=2))

# Simulate tool execution
tool_call = msg1["tool_calls"][0]
messages.append(msg1)
messages.append({
    "role": "tool",
    "tool_call_id": tool_call["id"],
    "name": tool_call["function"]["name"],
    "content": json.dumps({"hotels": [{"id": 1, "name": "Test Hotel", "base_price": 5000, "rating": 5, "review_count": 10, "location": "Bengaluru", "distance_info": "1km", "image_url": "url"}]})
})

payload["messages"] = messages
payload.pop("tools")
payload.pop("tool_choice")

response2 = requests.post(url, json=payload, headers=headers).json()
print("Second response:", json.dumps(response2, indent=2))
