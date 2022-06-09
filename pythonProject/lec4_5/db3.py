import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def connect_db(db_name):
    return sqlite3.connect(db_name)

def statistic(value):
    ans = []
    result = c.execute("select * from geo_stat").fetchall()
    for each in result:
        ans.append(each[value])
    return ans


conn = connect_db("geo_stat.sqlite")
conn.row_factory = sqlite3.Row
c = conn.cursor()

population = statistic('population')
birth = statistic('birth')
marriage = statistic('marriage')
divorce = statistic('divorce')
year = statistic('year')
print(population)
print(birth)
print(marriage)
print(divorce)

# plt.plot(year, population, marker='o', ls='--', c='b', label='population')
plt.plot(year, birth, marker='o', ls='--', c='m', label='birth')
plt.plot(year, marriage, marker='o', ls='--', c='g', label='marriage')
plt.plot(year, divorce, marker='o', ls='--', c='r', label='divorce')
plt.xticks(year)
plt.legend()
plt.ylabel('amount')
plt.xlabel('year')
plt.show()