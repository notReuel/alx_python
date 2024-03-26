import requests
import sys

URL = 'http://0.0.0.0:5000/search_user'

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

send = requests.post(URL, data={'q': q})

try:
    x=send.json()
    if not x: 
        print("No result")
    else: 
        print("[{}] {}".format(x['id'], x['name']))
except Exception as e:
    print("Not a valid JSON")


