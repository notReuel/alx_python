import requests

r = requests.get('https://alu-intranet.hbtn.io/status')

print("Body response:")
print(" - type: {}".format(type(r.text)))
print(" - content: {}".format(r.text))

