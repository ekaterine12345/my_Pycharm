import requests
import json
resp = requests.get('https://btu.edu.ge/')
# resp_png = requests.get('https://cdn.gweb.ge/buffer/1001285/pictures/slider/0eb215736a71d6aebcee359d1fa79554.png')
print(resp.text)
print(resp.headers['content-type'])
# print(resp_png.content)
# file = open('btu.png','wb')
# file.write(resp_png.content)

# city = 'Tbilisi'
# key = 'b0382a9da8d31051dd5eecdc220673dc'
# payload={}
# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&unit=metric'
# r = requests.get(url)
# print(r.text)

# city = 'Kutaisi'
# key = 'b0382a9da8d31051dd5eecdc220673dc'
# payload = {'q': city, 'appid': key, 'units': 'metric'}
# r = requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
# # print(r)
# # print(r.headers)
# print(r.json())