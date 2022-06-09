import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('codeforces.csv', 'w', encoding='UTF-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Code Name', 'Name', 'Score', 'Users'])


page = 1
while page <= 5:
    url = f'https://codeforces.com/problemset/page/{page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', class_='problems')
    tbody = table.find_all('tr')
    for each in tbody:
        if not each.td:
            continue
        info = each.find_all('td')
        code_name = info[0].a.text.strip()
        title = info[1].div.a.text.strip()
        score = info[3].text.strip()
        users = info[4].a.text.strip()
        if score == '':
            score = 'not graded'

        users = users.replace('x', '')
        print(code_name, title, score, users)
        file_obj.writerow([code_name, title, score, users])
    page += 1
    sleep(randint(2, 5))

file.close()
