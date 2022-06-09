import requests
import json
city = input("please enter the city: ")
key = 'b0382a9da8d31051dd5eecdc220673dc'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
r = requests.get(url)
# print(r.status_code)
# print(r.headers)
res = json.loads(r.text)
print(res)
print(json.dumps(res, indent=4))
print(type(r.text), type(r.json))
