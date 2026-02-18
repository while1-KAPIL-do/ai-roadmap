import json

def call_llm(messages):
    return {
        "choices": [
            {
                "message":{
                    "content": '{"priority": "high"}'
                }
            }
        ]
    }


message = [
    {
        "role": "system",
        "content": "You are classifier."
    },
    {
        "role": "user",
        "content": "classify ticket as JSON"
    }
]
response = call_llm(message)
choices = response.get("choices", [])

if not choices:
    print("model_failed")
else:
    content = choices[0].get("message", {}).get("content", "")

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"priority": "unknown"}

    priority = data.get("priority", "unknown")

    if priority not in ["high", "medium", "low"]:
        priority = "unknown"

    print(f"Ticket priority: {priority}")