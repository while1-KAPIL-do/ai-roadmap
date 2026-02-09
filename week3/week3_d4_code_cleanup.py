# make - 
    # Easier for other humans to read
    # Easier for future you to modify
    # Ready for GitHub review

# Reorder your file like this:
    # imports
    # helper functions (API)
    # business logic functions
    # main flow

print("__________________Refactor__________________", end="\n\n")

import requests



# ---------- API HELPERS ----------

def get_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error"     : "API Error",
            "message"   : str(e)
        }

def post_json(url, payload):
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error"     : "API Error",
            "message"   : str(e)
        }



# ---------- BUSINESS LOGIC ----------

def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    return get_json(url)

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
    return post_json(url, payload)



# ---------- MAIN ----------

def run_flow():
    user = fetch_user(1)
    payload = build_user_post_payload(user)
    post = create_post(payload)

    print("\n=== USER DATA ===")
    print(user)

    print("\n=== POST PAYLOAD ===")
    print(payload)

    print("\n=== POST RESPONSE ===")
    print(post)

run_flow()
    