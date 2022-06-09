from bs4 import BeautifulSoup
import requests

with open('sample.html', ) as file:
    content = file.read()

# print(content)

soup = BeautifulSoup(content, 'html.parser')
# print(soup)

nav = soup.find('nav')

unis = nav.find('ul')
list_items = unis.find_all('li')

uni_list = []

for each in list_items:
    uni = each.find('a').text
    uni_list.append(uni)

print(uni_list)

footer = soup.find('footer')
google_log = footer.find('img').attrs['src']
print(google_log)

r = requests.get(google_log)

with open('stat/google.png', 'wb') as f:
    f.write(r.content)


