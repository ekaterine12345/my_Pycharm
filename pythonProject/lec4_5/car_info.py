import sqlite3


class Car:
    def __init__(self, car_id, manufacture, model):
        self.car_id = car_id
        self.manufacture = manufacture
        self.model = model


class Info:
    def __init__(self, cid, color, date, price):
        self.cid = cid
        self.color = color
        self.date = date
        self.price = price


def connect_db(db_name):
    return sqlite3.connect(db_name)


def get_all_records_car():
    cur.execute("select * from cars2 inner join info ON cars2.car_id=info.cid")
    records = cur.fetchall()
    conn.commit()
    for each in records:
        print(each)


def creat_carDB():
    cur.execute('''CREATE TABLE cars2
    (car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacture VARCHAR(50),
    model VARCHAR(100));''')
    conn.commit()


def  creat_infoDB():
    cur.execute('''CREATE TABLE info
    (cid INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(50),
    date VARCHAR(100), 
    price FLOAT);''')
    conn.commit()


def add_car( manufacture, model, color, date, price):
    id = cur.execute("SELECT count(car_id) from cars2").fetchone()[0]
    id += 1
    cur.execute('INSERT INTO cars2 (car_id, manufacture, model) VALUES (?,?,?) ', (id, manufacture, model))
    conn.commit()
    cur.execute('INSERT INTO info (cid, color, date, price) VALUES (?,?,?,?) ', (id, color, date, price))
    conn.commit()
    print("ჩანაწერი წარმატებით დაემეტა!")


def delete_car(car_id):
    cur.execute("DELETE FROM cars2 WHERE car_id=?", (car_id,))
    conn.commit()
    cur.execute("DELETE FROM info WHERE cid=?", (car_id,))
    conn.commit()
    print("ჩანაწერი წარმატებით წაიშალა!")


def update_record(id, manufacture, model, color, date, price):
    cur.execute('UPDATE cars2 SET manufacture=?,model=? WHERE car_id=?', (manufacture, model, id))
    conn.commit()
    cur.execute('UPDATE info SET color=?,date=?, price=? WHERE cid=?', (color, date, price, id))
    conn.commit()
    print("ჩანაწერი წარმატებით შეიცვალა!")

conn = connect_db("my_database1.sqlite")
cur = conn.cursor()
#creat_infoDB()
#delete_car(5)
add_car("manu13", "xmxmxmnm", "red", "12-03-2005", 2034)
get_all_records_car()
update_record(1, "manu4", "3232", "blue", '12-04-2007', 3432)
get_all_records_car()

