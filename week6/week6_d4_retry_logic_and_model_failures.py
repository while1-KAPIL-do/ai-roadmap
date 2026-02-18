# # Types of Failures You Must Expect
# Network failure
# Empty response
# Invalid JSON
# Wrong format
# Timeout
# Rate limit

import josn

# Step 1 — Basic Retry Pattern
def safe_call_llm(message, retries = 3):
    for attempt in range(retries):
        try:
            response = call_llm(message)
            return response
        except Exception:
            print("Retrying...")
    return None
# # Why retry?
# Because sometimes second try works.
# APIs are not perfect.


# Step 2 — Combine With JSON Parsing
response = safe_call_llm(message)
if not response:
    print('model_failed')
else:
    content = response.get("choices", [])[0].get('message', {}).get("content", "")
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"priority": "unknown"}
    print(data)


# Step 3 — Add Delay Between Retries

import time

def safe_call_llm(messages, retries=3):
    for attempt in range(retries):
        try:
            return call_llm(messages)
        except Exception:
            time.sleep(1)  # wait 1 second
    return None


# # System Maturity Upgrade
# Before:
# Call model → hope it works
# Now:
# Call model → retry → validate → fallback


# # Practice Exercise
# Modify call_llm() to randomly fail:

import random

def exercise_call_llm(messages):
    if random.choice([True, False]):
        raise Exception("Temporary failure")

    return {
        "choices": [
            {
                "message": {
                    "content": '{"priority": "medium"}'
                }
            }
        ]
    }


def exercise_safe_call_llm(messages, retries=3):
    for attempt in range(retries):
        try:
            return exercise_call_llm(messages)
        except Exception:
            time.sleep(1)  # wait 1 second
    return None


response = exercise_safe_call_llm(message)

if not response:
    print('model_failed')
else:
    content = response.get("choices", [])[0].get('message', {}).get("content", "")

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"priority": "unknown"}

    print(data)