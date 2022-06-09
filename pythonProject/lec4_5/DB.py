import sqlite3
conn = sqlite3.connect("my_database.sqlite")
cursor = conn.cursor()


# cursor.execute('''CREATE TABLE books
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  title VARCHAR(50),
#                  author VARCHAR(100),
#                  price FLOAT)
#                 ''')

# book_list = [
#     ('The Book Thief', 'Markus Zusak', 17),
#     ('Animal Farm', 'George Orwell', 13),
#     ('The Hunger Games', 'Suzanne Collins', 17),
#     ('Harry Potter and the Prisoner of Azkaban', 'Rowling',  25),
#     ('Harry Potter and the Goblet of Fire', 'Rowling', 24),
#     ('Macbeth', 'William Shakespeare', 29)
# ]
# cursor.executemany("INSERT INTO books (title, author, price) VALUES  (?, ?, ?)", book_list)

cursor.execute('''select * from  books
                    where title='Animal Farm'
                ''')

records = cursor.fetchall()
print(records)
conn.commit()

conn.close()
