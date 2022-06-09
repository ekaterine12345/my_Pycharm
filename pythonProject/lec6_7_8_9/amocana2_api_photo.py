import requests
import json
key = 'Qoqjehlm0x1ObydBthVW9vc5k4sWJaSJmDjn0avp'
year = int(input("enter year: "))
month = int(input("enter month: "))
day = int(input("enter day: "))
payload = {'api_key': key, 'date': f'{year}-{month}-{day}'}
r = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
res = r.json()  # res-ში წერია ლექსილონი dict-ი
print(type(res))
print("This Date's JSON")
print(json.dumps(res, indent=4))
imag_url = res['url']
r_imag = requests.get(imag_url)
print(r_imag)
with open('nasa.png', 'wb') as f:
    f.write(r_imag.content)


# account_id='54dfad06-d365-491d-8240-79b8ea602732'