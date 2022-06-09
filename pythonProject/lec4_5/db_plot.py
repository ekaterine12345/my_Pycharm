import sqlite3
import matplotlib.pyplot as plt
import numpy as np


# def connect_db(db_name):
#     return sqlite3.connect(db_name)
#
# def statistic(value):
#     ans = []
#     result = c.execute("select * from geo_stat").fetchall()
#     for each in result:
#         ans.append(each[value])
#     return ans
#
#
# conn = connect_db("geo_stat.sqlite")
# conn.row_factory = sqlite3.Row
# c = conn.cursor()
#
# population = statistic('population')
# birth = statistic('birth')
# marriage = statistic('marriage')
# divorce = statistic('divorce')
# year = statistic('year')
# print(population)
# print(birth)
# print(marriage)
# print(divorce)

x_points = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y1_total = [52_442, 56_568, 55_230, 51_565, 49_969, 49_657, 60_635, 59_249, 56_569, 53_293, 51_138, 48_296]

y2_boys = [27698, 29660, 28787, 26942, 26138, 25747, 31325,  30902, 28887, 27658, 26538, 24600]
y3_girls = [24744, 26908, 26443, 24623, 23831, 23910, 29310,  28347, 27682, 25635, 24600, 23267]
plt.plot(x_points, y1_total, marker='o', ls='--', c='g', label="both")
plt.plot(x_points, y2_boys, marker='o', ls='--', c='b', label="boys")
plt.plot(x_points, y3_girls, marker='o', ls='--', c='m', label="girls")

plt.ylabel('amount')
plt.xlabel('year')
plt.xticks(x_points)
plt.legend()
# plt.savefig()
plt.show()