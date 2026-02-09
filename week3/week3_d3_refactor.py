print("__________________Refactor__________________", end="\n\n")

import requests

def safe_get(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error"     : "API Error",
            "message"   : str(e)
        }

def safe_post(url, payload):
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error"     : "API Error",
            "message"   : str(e)
        }

def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    return safe_get(url)

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
    return safe_post(url, payload)

def main():
    user = fetch_user(1)
    payload = build_user_post_payload(user)
    post = create_post(payload)

    print("USER:")
    print(user)
    print("\nPAYLOAD:")
    print(payload)
    print("\nPOST:")
    print(post)

main()
    