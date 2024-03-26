import requests
import sys

URL = 'https://api.github.com/user/${username}'

def get_github_user(username, token):
    url = f"https://api.github.com/user/{username}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print("failed to return access user data, Error code {response.status_code}")
        return None
        

