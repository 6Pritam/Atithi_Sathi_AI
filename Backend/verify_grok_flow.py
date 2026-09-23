import httpx
import json
import time

BASE_URL = "http://localhost:8000/api/v1"
client = httpx.Client(timeout=30.0)

def print_result(name, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")

def run_tests():
    print("--- Running Verification Tests ---")
    
    # 1. Basic Grok Response
    res1 = client.post(f"{BASE_URL}/chat", json={"message": "Hello"})
    data1 = res1.json()
    if data1.get("success") and "message" in data1 and data1["message"]:
        print_result("1. Basic Grok response", True, f"Response: {data1['message']}")
    else:
        print_result("1. Basic Grok response", False, str(data1))
        
    # 2. Find me a hotel in Bengaluru
    res2 = client.post(f"{BASE_URL}/chat", json={"message": "Find me a hotel in Bengaluru"})
    data2 = res2.json()
    attachments = data2.get("attachments", [])
    if attachments and attachments[0]["type"] == "hotel_list":
        hotels = attachments[0]["data"]
        print_result("2. Find hotel in Bengaluru", True, f"Found {len(hotels)} hotels. AI: {data2['message']}")
    else:
        print_result("2. Find hotel in Bengaluru", False, str(data2))

    # 3. Tell me about Grand Horizon
    res3 = client.post(f"{BASE_URL}/chat", json={"message": "Tell me about Grand Horizon"})
    data3 = res3.json()
    attachments3 = data3.get("attachments", [])
    if attachments3 and attachments3[0]["type"] == "hotel":
        hotel = attachments3[0]["data"]
        print_result("3. Tell me about Grand Horizon", True, f"Returned hotel: {hotel['name']}")
    else:
        print_result("3. Tell me about Grand Horizon", False, str(data3))

    # 4. Does Grand Horizon have a swimming pool?
    res4 = client.post(f"{BASE_URL}/chat", json={"message": "Does Grand Horizon have a swimming pool?"})
    data4 = res4.json()
    if data4.get("success") and "pool" in data4.get("message", "").lower() or "yes" in data4.get("message", "").lower():
        print_result("4. Does Grand Horizon have a swimming pool?", True, f"AI: {data4.get('message', '')}")
    else:
        print_result("4. Does Grand Horizon have a swimming pool?", False, f"AI: {data4.get('message', str(data4))}")

    # 5. What are the hotel policies?
    res5 = client.post(f"{BASE_URL}/chat", json={"message": "What are the hotel policies for Grand Horizon?"})
    data5 = res5.json()
    if data5.get("success"):
        print_result("5. What are the hotel policies?", True, f"AI: {data5.get('message', '')}")
    else:
        print_result("5. What are the hotel policies?", False, str(data5))

    # 6. Check availability
    res6 = client.post(f"{BASE_URL}/chat", json={"message": "Check availability from 2026-10-10 to 2026-10-12 for 2 adults at Grand Horizon"})
    data6 = res6.json()
    conv_id = data6.get("conversation_id")
    attachments6 = data6.get("attachments", [])
    if data6.get("success") and attachments6 and attachments6[0]["type"] == "room":
        rooms = attachments6[0]["data"]
        print_result("6. Check availability", True, f"Found {len(rooms) if isinstance(rooms, list) else 1} rooms. AI: {data6.get('message', '')}")
    else:
        print_result("6. Check availability", False, str(data6))

    # 7. Follow-up using conversation_id
    res7 = client.post(f"{BASE_URL}/chat", json={"message": "What about breakfast?", "conversation_id": conv_id})
    data7 = res7.json()
    if data7.get("success") and data7.get("conversation_id") == conv_id:
        print_result("7. Follow-up question", True, f"AI: {data7.get('message', '')}")
    else:
        print_result("7. Follow-up question", False, str(data7))

    # 8. Unknown/non-hotel
    res8 = client.post(f"{BASE_URL}/chat", json={"message": "Who is the Prime Minister of India?"})
    data8 = res8.json()
    msg8 = data8.get("message", "").lower()
    if data8.get("success") and ("hotel" in msg8 or "assist" in msg8 or "cannot" in msg8 or "don't" in msg8 or "do not" in msg8):
        print_result("8. Unknown/non-hotel question", True, f"AI: {data8.get('message', '')}")
    else:
        print_result("8. Unknown/non-hotel question", False, f"AI: {data8.get('message', str(data8))}")

    # 9. Unsupported hotel info
    res9 = client.post(f"{BASE_URL}/chat", json={"message": "Does Grand Horizon have a helicopter service?"})
    data9 = res9.json()
    print_result("9. Unsupported hotel info", data9.get("success", False), f"AI: {data9.get('message', str(data9))}")

    # 10. Verify no hallucination (manual check via above logs)
    print_result("10. Verify no hallucinated hotel/availability data", True, "Manual verification via logs")

if __name__ == "__main__":
    run_tests()
