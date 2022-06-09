import sqlite3
conn = sqlite3.connect("book_db.sqlite")
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE books
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  title VARCHAR(50),
#                  author VARCHAR(100),
#                  price FLOAT)
#                 ''')


def db(s):
    cursor.execute(s)
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.commit()
    print()


db("select * from books where author='William Shakespeare'")
db("select * from books where author='William Shakespeare' or author='Rowling'")
db("select * from books where price<=20")
db("SELECT DISTINCT author FROM books")
db("SELECT username FROM users where balance>100")
db('''SELECT b.id,b.title,b.author,b.price,p.purchase_date FROM books b
      INNER JOIN purchase p
      WHERE (b.id=p.book_id AND p.purchase_date<'2018-01-01')
      order by b.id
    ''')

db('''SELECT u.id,u.username,u.balance,p.purchase_date FROM users u
      INNER JOIN purchase p
      WHERE (u.id=p.user_id AND p.purchase_date BETWEEN '2018-01-01' and '2018-12-31')
      order by u.id
    ''')

db('''SELECT u.id,u.username,u.balance,p.purchase_date FROM users u
      INNER JOIN purchase p
      WHERE u.id=p.user_id
      ORDER BY u.id
    ''')

db('''SELECT b.id,b.title,b.author,b.price,p.purchase_date FROM books b
      INNER JOIN purchase p
      ON b.id=p.book_id
      ORDER BY b.id
    ''')

db('''SELECT b.id,b.title,b.author,b.price,p.purchase_date FROM books b
      LEFT JOIN purchase p
      ON b.id=p.book_id
      WHERE p.purchase_date IS NULL
      ORDER BY b.id;
    ''')

db('''SELECT u.id,u.username,u.balance,p.purchase_date,b.title FROM users u
      INNER JOIN purchase p ON u.id=p.user_id
      INNER JOIN books b ON b.id=p.book_id
      ORDER BY u.id;
    ''')
conn.close()
