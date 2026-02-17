# Real LLM Message-Based Calling – Backend Flow

---

## Real LLM Calls Usually Follow This Idea

You send:

```json
{
  "model": "...",
  "messages": [...]
}
```

---

## Messages Are Conversation Objects

Instead of one prompt string.

Example:

```json
[
  {"role": "system", "content": "You are helpful"},
  {"role": "user", "content": "Explain APIs"}
]
```

System → rules  
User → task  

---

# Python Example (Simplified)

```python
def call_llm(messages):
    return {
        "choices": [
            {
                "message": {
                    "content": "API enables communication between systems"
                }
            }
        ]
    }
```

---

## Extracting Answer (Here Is Where Beginners Panic)

```python
response = call_llm(messages)
answer = response["choices"][0]["message"]["content"]
print(answer)
```

---

## What If:

1. choices missing?  
2. list empty?  
3. message missing?  

Boom → crash.

---

## Mental Model You Must Lock

LLM response = nested JSON  
Your job = safely walk inside it.

---

## Like Walking Through Folders

```
response
 └── choices (list)
      └── first item [0]
            └── message (dict)
                  └── content (string)
```

---

# Safe Extraction Pattern (VERY IMPORTANT)

```python
choices = response.get("choices", [])

if not choices:
    print("model_failed")
else:
    message = choices[0].get("message", {})
    content = message.get("content", "unknown")
    print(content)
```

Because sometimes it can return multiple answers.  
We usually pick the first.

---

# Architecture Reminder

Backend  
↓  
Build messages  
↓  
Call API  
↓  
Extract content  
↓  
Use it  

---

# Full Example

```python
def call_llm(messages):
    # call llm api with messages
    return {
        "choices": [
            {
                "message": {
                    "content": "JSON is a data format."
                }
            }
        ]
    }

messages = [
    {"role": "system", "content": "You are backend tutor."},
    {"role": "user", "content": "Explain JSON in one line."}
]

response = call_llm(messages)
choices = response.get("choices", [])

if not choices:
    print("model_failed")
else:
    message = choices[0].get("message", {})
    content = message.get("content", "unknown")
    print(content)
```
