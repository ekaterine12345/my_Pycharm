import requests
from bs4 import BeautifulSoup
import json
url = "https://www.moh.gov.ge/ka/feedback/?fbclid=IwAR0xOtGXu2R5XCyR2r6E91QhAn0T2bLeqdriCcvDA1TsrD5pg7BGpq3InTA"
r = requests.get(url)
print(r)
content = r.text
soup = BeautifulSoup(content, 'html.parser')

sec = soup.find('section', {'class': 'contact'})
un_list = sec.find('ul')
items = un_list.find_all('li')
address = items[0].text
mobile = items[1].text
email = items[2].text

dict = {address[0:9]: address[12:], mobile[0:8]: mobile[10:], email[0:8]: email[11:]}
print(dict)

with open('contact.json', 'w', ) as f:
    json.dump(dict, f,  indent=4)
