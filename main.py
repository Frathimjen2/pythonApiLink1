import requests
import json

r = requests.get("https://api1wordbank.retool.com/editor/Onboarding%20Page")
j=r.json()
print(j)
