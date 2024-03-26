import requests
import sys


'''
sending an email using request and sys argv
'''
if len(sys.argv) > 1:
    URL = sys.argv[1]
    email = sys.argv[2]

req = requests.post(URL, data={'email': email})
print(req.text)