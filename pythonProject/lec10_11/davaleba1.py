import requests
from bs4 import BeautifulSoup
import csv
file = open('countries.csv', 'w', encoding='UTF-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['რიგითი ნომერი', 'ქვეყანა', 'მოსახლეობა', 'ფართობი (კვ.მ.)'])
url = "https://www.worldometers.info/world-population/population-by-country/"
r = requests.get(url)
print(r)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
tbody = soup.find('tbody')
all_countries = tbody.find_all('tr')
for each in all_countries:
    info = each.find_all('td')
    position = info[0].text
    country = info[1].text
    population = info[2].text
    land_area = info[6].text
    print(position, country, population, land_area)
    file_obj.writerow([position, country, population, land_area])

file.close()
