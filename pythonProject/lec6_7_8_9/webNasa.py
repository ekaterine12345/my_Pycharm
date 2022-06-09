import requests
import json
key = 'v4teSmMaW4h8fggkyFWSa7VaVDhmvGBMljA0Fewe'
palyload = {'api_key', key}
r = requests.get('https://api.nasa.gov/planetary/apod', params=palyload)
res = json.loads(r.text)