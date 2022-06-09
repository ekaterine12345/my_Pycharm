import sqlite3


conn = sqlite3.connect("movies_ranking.sqlite")
cur = conn.cursor()
ans = cur.execute("select * from movies").fetchall()

for each in ans:
    print(each)

cur.execute("INSERT INTO movies (Film, Genre, LeadStudio, WorldWideGross, Year) VALUES (?,?,?,?,?)", ('F1', 'G1', 'LS1', 'FFF', 2012))
conn.commit()

conn.close()

