'''
A module to get a response from a url.
url - Uniform Resource Locator
'''
import requests

r = requests.get('https://alu-intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))

