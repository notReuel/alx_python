import requests
import sys

if len(sys.argv) > 1:
    URL = sys.argv[1]

req = requests.get(URL) 
status = req.status_code

if status >= 400:
    print("Error code: {}".format(status))
else:
    print(req.text)