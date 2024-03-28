import requests
import sys


if len(sys.argv) > 1:
    username = sys.argv[1]
    pwd = sys.argv[2]

URL = 'https://api.github.com/user/'

try:
    res = requests.get(URL, auth=(username,pwd))
    res_json = res.json()
    print(res_json['id'])
except Exception as e:
    print('None')
    



