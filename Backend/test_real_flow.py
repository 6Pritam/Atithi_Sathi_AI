import httpx
import json

client = httpx.Client(timeout=30)
response = client.post('http://localhost:8000/api/v1/chat', json={'message': 'Find me a hotel in Indiranagar'})

data = response.json()
print("Success:", data.get("success"))
print("Message:", data.get("message").encode('utf-8', 'ignore').decode('utf-8'))
if data.get("attachments"):
    print("Attachments:", json.dumps(data.get("attachments"), indent=2))
else:
    print("No attachments.")
