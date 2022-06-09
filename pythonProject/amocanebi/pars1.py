from bs4 import BeautifulSoup
import requests

with open('sample2.html', ) as file:
    content = file.read()

# print(content)

soup = BeautifulSoup(content, 'html.parser')

nav = soup.find('nav')
unorderd_list = nav.find_all('ul')[1]
all_cities = unorderd_list.find_all('li')
cities=[]

for each in all_cities:
    cities.append(each.text)

print(cities)

trows = soup.find_all('tr')[1]
tr1= trows.find_all('td')[1].text
tr2 = trows.find_all('td')[2].text
print(tr1[0:4], tr2[0:4])
sum = int(tr1[0:4])+int(tr2[0:4])
print(sum)