import sqlite3
import matplotlib.pyplot as plt

def fun(year, genre):
    c = cur.execute("select * from games where genre=? and year=?", (genre, year)).fetchall()
    conn.commit()
    return c


conn = sqlite3.connect("topgames.sqlite")
cur = conn.cursor()

c1 = cur.execute("select name from games where userScore>8").fetchall()

for each in c1:
    print(each)

print()
c2 = fun(2010, 'Party')
for each in c2:
    print(each)

print()
c3 = cur.execute("select distinct Publisher from games").fetchall()

for each in c3:
    print(each)


cur.execute('''INSERT INTO games(name, genre, ESRBRating, Platform, Publisher, criticScore, userScore, year) 
               VALUES (?,?,?,?,?,?,?,?)''', ("n1", "Party", 'E', 'Wii', 'Microsoft Game Studios', 5, 5, 2010) )
conn.commit()

x = []
y = []
x = cur.execute("select count(*) from games group by year order by year").fetchall()
y = cur.execute("select distinct year from games order by year").fetchall()

plt.plot(y, x, marker='o', ls='--', c='g', label="games")
plt.legend()
plt.show()
# tito wels ramdeni tamashi gamovisa
conn.close()
