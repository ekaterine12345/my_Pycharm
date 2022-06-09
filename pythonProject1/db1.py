import sqlite3
conn = sqlite3.connect("my_database.sqlite")
cursor = conn.cursor()

cursor.execute('''select * from  books
                    where title='Animal Farm'
                ''')
conn.commit()