# This is the same pattern as:
#     Sending prompt to OpenAI
#     Sending query to RAG service
#     Sending tool input to agent

print("__________________POST REQUESTS__________________", end="\n\n")

import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title" : "AI Engineer Roadmap",
    "body"  : "Learning APIs with Python",
    "userId": 1
}

response = requests.post(url, json=payload)
print(response)
print(response.status_code)
print(response.text)

# RESPONSE → DICTIONARY
data = response.json()
print(data)
print(data['id'])

# ERROR HANDLING
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title" : "AI Engineer Roadmap",
    "body"  : "Learning APIs with Python",
    "userId": 1
}
try:
    response = requests.post(url, json=payload)
    data = response.json()
    print("Post created with id : ", data.get("id"))
except requests.exceptions.RequestException as e:
    print("POST request failed:", e)

# FUNCTION VERSION
def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title" : title,
        "body"  : body,
        "userId": user_id,
    }
    try:
        response = requests.post(url, json=payload)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

p1 = create_post("AAAAAA", "TEST body AAAAAA", 1)
p2 = create_post("BBBBBB", "TEST body BBBBBB", 2)
p3 = create_post("CCCCCC", "TEST body CCCCCC", 3)
print(p1,p2,p3)
print("___________________________________________________", end="\n\n")





