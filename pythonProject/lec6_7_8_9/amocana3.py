import requests
import json
r = requests.get('https://api.spacexdata.com/v3/capsules')
# print(r.text)
res = r.json()
print(json.dumps(res, indent=4))
print(res[0]['capsule_serial'])


# https://docs.spacexdata.com/?version=latest