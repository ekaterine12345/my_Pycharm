import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('imdb.csv', 'w', encoding='UTF-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Year', 'Ranking'])

p = {'groups': 'top_250', 'start': 1}
h = {'Accept-Language': 'en-US'}
url = 'https://www.imdb.com/search/title/'

while p['start'] < 251:
    r = requests.get(url, params=p, headers=h)
    # print(r.headers)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('div', class_='lister-list')
    all_movies = block.find_all('div', class_='lister-item')
    for each in all_movies:
        title = each.h3.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        ranking = each.strong.text
        print(title, year, ranking)
        file_obj.writerow([title, year, ranking])
    p['start'] += 50
    sleep(randint(2, 5))
    print()

file.close()
