
print("__________________GET APIs__________________", end="\n\n")

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)
print(response.text) # to string

data = response.json() # to py-dict
print(data)
print(data['title'])



print("__________________Exeption and method__________________", end="\n\n")

try:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("API Exception - ", e)

def get_post_titile(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("title", "No Title")
    except requests.exceptions.RequestException:
        return "API error"

print(get_post_titile(2))
print(get_post_titile(3))



print("__________________Sample__________________", end="\n\n")


def get_user_by_id(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        return "API error"

print(get_user_by_id(1))


print("__________________Pretty print__________________", end="\n\n")

import json
user = get_user_by_id(2)
print(json.dumps(user, indent=4))


