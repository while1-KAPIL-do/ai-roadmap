print("__________________API REAL FLOW__________________", end="\n\n")

import requests

def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        {
            "error" : "API error",
            "message" : str(e)
        }

def build_user_post_payload(user):
    if not user:
        return {"error": "User Not found"}

    return {
        "title"     : f"Post by {user.get('name', 'Unknown')}",
        "body"      : f"Email {user.get('email', 'N/A')}",
        "userId"    : user.get("id", 0)
    }

def create_post(payload):
    if not payload:
        return {"error": "Invalid payload"}

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error" : "API error",
            "message" : str(e)
        }
    
user    = fetch_user(1)
payload = build_user_post_payload(user)
post    = create_post(payload)

print(user)
print("------------------------")
print(payload)
print("------------------------")
print(post)
