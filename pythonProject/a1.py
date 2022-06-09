import requests
import json
from bs4 import BeautifulSoup

url = "https://www.mes.gov.ge/content.php?id=6&lang=geo&fbclid=IwAR07Qzka6M6qUC8l0SKGZiqNccpCF7ECUzTLrma2VTPEqSQhkJLJqF6bNkI"
r = requests.get(url)
print(r)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
info = soup.find('div', {'class': 'contactinfo'})
info_list = info.find_all('p')
dict = {}
k = 0
for each in info_list:
    k += 1
    print(each.find('span').text)
    dict[f'info{k}'] = each.find('span').text

# address = info_list.find.find('span').text
# number = info_list.find('span', {'class': 'fa-phone-square'}).text
# email = info_list.find('span', {'class': 'fa-fax'}).text
# print(address, number, email)
with open('stopCov.json', 'w', ) as f:
    json.dump(dict, f,  indent=4)
