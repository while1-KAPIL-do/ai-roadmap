print("__________________PRACTICE__________________", end="\n\n")

import requests

def get_user_name(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("name", "Unknown")
    except requests.exceptions.RequestException as e :
        return "API Error : ", e

print(get_user_name(1))



def get_post_title(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("title", "Unknown")
    except requests.exceptions.RequestException as e:
        return "API Error : ", e

print(get_post_title(1))


def get_user_info(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'name' : data.get("name", "Unknown"),
            'email' : data.get("email", "Not provided"),
            'city' : data.get("address", {}).get("city", "Unknown"),
        }    
    except requests.exceptions.RequestException as e :
        return "API Error : ", e

print(get_user_info(1))
