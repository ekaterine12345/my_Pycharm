import sqlite3


def creat_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS students
               (id  INTEGER PRIMARY KEY AUTOINCREMENT,
               age INTEGER,
               onlineClassTime FLOAT,
               device VARCHAR(50),
               selfStudyHour float,
               fitnessTime float,
               sleep float,
               socialMedia float,
               socialMediaPlatfrom  VARCHAR(50),
               weight VARCHAR (50),
               ManageStressMethod VARCHAR (50),
               WhatYouMissed VARCHAR (50))''')

    conn.commit()


def fun(socialMediaPlatfrom, age):
    c2 = cur.execute("select count(*) from students where socialMediaPlatfrom=? and age=?", (socialMediaPlatfrom, age)).fetchone()
    conn.commit()
    return c2


conn = sqlite3.connect("survey1.sqlite")
cur = conn.cursor()
creat_table()

c1 = cur.execute("select count(*) from students where selfStudyHour>5").fetchone()
print(c1)
conn.commit()

print(fun("instagram", 19))

c3 = cur.execute("select distinct ManageStressMethod from students").fetchall()
print(c3)
conn.commit()

cur.execute('''INSERT INTO students (age, onlineClassTime, device, selfStudyHour, fitnessTime, sleep,
               socialMedia,  socialMediaPlatfrom, weight, ManageStressMethod, WhatYouMissed )
               values(?,?,?,?,?,?,?,?,?,?,?)''', (19, 30, "leptop", 3, 0, 8, 1, "instagram", "bbb", "none ggt r", "nothing"))
conn.commit()
conn.close()
