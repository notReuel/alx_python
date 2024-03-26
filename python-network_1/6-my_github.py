import requests
import sys

URL = 'https://api.github.com/user/${username}'

if len(sys.argv) > 1:
    username = sys.argv[1]
    pwd = sys.argv[2]

    try:
        res = requests.get(URL, auth=(username,pwd))
        res_json = res.json()
        print(res_json)
    except Exception as e:
        print('None')
    



