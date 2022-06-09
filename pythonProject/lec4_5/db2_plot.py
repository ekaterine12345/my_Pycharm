import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def connect_db(db_name):
    return sqlite3.connect(db_name)


def percent(a, b=891):
    return a/b*100


def gender(gender):
    c.execute("SELECT count(*) FROM Passengers WHERE Sex=?", (gender,))
    return c.fetchone()[0]


def gender_surv(gender,surv):
    c.execute("SELECT count(*) FROM Passengers WHERE Sex=? AND Survived=?", (gender, surv))
    return c.fetchone()[0]


def Pcllas_count(Pclass):
    c.execute("SELECT count(*) FROM Passengers WHERE Pclass=?", (Pclass, ))
    return c.fetchone()[0]


def pclass_average_cost(Pclass):
    c.execute("SELECT sum(Fare)/count(PassengerId) FROM Passengers WHERE Pclass=?", (Pclass,))
    return c.fetchone()[0]


conn = connect_db("Titanic.sqlite")
c = conn.cursor()
female = gender('female')
male = gender('male')
female_surv = gender_surv('female', 1)
female_not_surv = gender_surv('female', 0)
male_surv = gender_surv('male', 1)
male_not_surv = gender_surv('male', 0)
print("Female Passengers:", female, percent(female))
print("Male Passengers:", male, percent(male))
print("Female Survived Passengers:", female_surv, percent(female_surv) )
print("Female Not Survived Passengers:", female_not_surv, percent(female_not_surv))
print("Male Survived Passengers:", male_surv, percent(male_surv))
print("Male Not Survived Passengers:", male_not_surv, percent(male_not_surv))

p1 = Pcllas_count(1)
p2 = Pcllas_count(2)
p3 = Pcllas_count(3)
p1_average = pclass_average_cost(1)
p2_average = pclass_average_cost(2)
p3_average = pclass_average_cost(3)
print("First Class Passengers:", p1, percent(p1), p1_average)
print("Second Class Passengers:", p2, percent(p2), p2_average)
print("Third Class Passengers:", p3, percent(p3), p3_average)
conn.close()


labels = 'female survived', 'female not survived', 'male survived', 'male not survived'
sizes = [female_surv, female_not_surv, male_surv, male_not_surv]

fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
# fig3, ax3 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# ax2.pie([female, male], labels=('females', 'males'), autopct='%1.1f%%', startangle=90)
# ax3.pie([p1, p2, p3], labels=('First ', 'Seocnd', 'Third'), autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
#ax2.axis('equal')

labels2 = ['survived', 'not survived']
men_means = [male_surv, male_not_surv]
women_means = [female_surv, female_not_surv]

x = np.arange(len(labels2))  # the label locations


width = 0.35  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - width/2, men_means, width, label='Male')
rects2 = ax.bar(x + width/2, women_means, width, label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels2)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
