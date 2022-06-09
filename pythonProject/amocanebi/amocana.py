from bs4 import BeautifulSoup
import requests

url = "https://www.palitral.ge/?fbclid=IwAR2PiloXC__N3sYw1aIm69G1ZeZfwroMQymUaNTP3sp7bj83zJs93QWgOuY"
r = requests.get(url)
print(r)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
unordered_list = soup.find('ul')
list_items = unordered_list.find_all('li')
for each in list_items:
    print(each.text)
