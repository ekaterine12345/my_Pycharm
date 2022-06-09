import requests
from bs4 import BeautifulSoup

file = open('books.csv', 'w', encoding='UTF-8_sig')
file.write('სათაური,ავტორი,ფასი'+'\n')
url = "https://www.lit.ge/index.php?page=books&send[shop.catalog][order]=1&send[shop.catalog][reset]=1"
r = requests.get(url)
print(r)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
# print(soup)
section = soup.find('section', {'class': 'list-holder'})
all_books = section.find_all('article', {'class': 'item-holder'})
for each in all_books:
    t_bar = each.find('div', {'class': 'title-bar'})
    title = t_bar.a.text
    author = t_bar.span.b.a.text

    price = each.button.text.strip()
    print(title, author, price)
    file.write(title + ',' + author + ',' + price+'\n')

file.close()
# print(section)

