import requests
import sys

if len(sys.argv) > 1:
    URL = sys.argv[1]

req = requests.get(URL)  
print(req.headers.get('x-Request-Id'))