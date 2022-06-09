import sqlite3
import matplotlib.pyplot as plt


def connect_db(db_name):
    return sqlite3.connect(db_name)


# ამოცანა 2
def read_record(year1, year2, gender):
    cur.execute('''SELECT count(id) FROM oscar WHERE year between ? AND ? AND gender=?''', (year1, year2, gender))
    conn.commit()
    return cur.fetchone()[0]
# ფუნქცია read_record-ით ვითვლი რაიმე ორ წელს შორის აღებული ოსკარების რაოდენობას სქესის მიხედვით


# ამ ფუნქციის გამოძახებისას იბეჭდება ბაზაში არსებული oscar ცხრილის ყველა ჩანაწერო
def get_all_records():
    cur.execute("select * from oscar")
    records = cur.fetchall()
    conn.commit()
    for each in records:
        print(each)


# ამოცანა 3
def add_record(year, age, name, gender, movie):
    id = cur.execute("SELECT count(id) from oscar").fetchone()[0]
    id += 1
    cur.execute('INSERT INTO oscar (id, year, age, name, gender, movie) VALUES (?,?,?,?,?,?) ', (id, year, age, name, gender, movie))
    conn.commit()
    print("ჩანაწერი წარმატებით დაემეტა!")


# ამოცანა 4
def update_record(id, year, age, name, gender, movie):
    cur.execute('UPDATE oscar SET year=?, age=?, name=?, gender=?, movie=? WHERE id=?', (year, age, name, gender, movie, id))
    conn.commit()
    print("ჩანაწერი წარმატებით შეიცვალა!")


conn = connect_db("oscar_winners.sqlite")
cur = conn.cursor()
female_century20 = read_record(1900, 1999, 'F')
male_century20 = read_record(1900, 1999, 'M')
female_century21 = read_record(2000, 2099, 'F')
male_century21 = read_record(2000, 2099, 'M')
# ვითვლი 20 და 21 საუკუნეებიში რამდენმა ქალმა/კაცმა აიღო ოსკარი და შემდგომ ამის მიხედვით ვაგებ დიაგრამას
# ამოცანა 5
# print(female_century20, male_century20, female_century21, male_century21)
print(f"მე-20 საუკუნეში ოსკარი აიღო {female_century20} ქალმა")
print(f"მე-21 საუკუნეში ოსკარი აიღო {female_century21} ქალმა")
print(f"მე-20 საუკუნეში ოსკარი აიღო {male_century20} კაცმა")
print(f"მე-21 საუკუნეში ოსკარი აიღო {male_century21} კაცმა")
labels = 'female 20th century', 'female 21th century', 'male 20th century', 'male 21th century'
sizes = [female_century20, female_century21, male_century20, male_century21]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

# ამოცანა 3
# მომხმარებელს ვეკითხები სურს თუ არა ცხრილში ახალი ჩანაწერის დამატება და დადასტურების შემთხვევაში (თუ 1-იანი შეიყვანა)
# ვკითხულობ მის მიერ შეყვანილ მონაცემებს და გადავცემ add_record ფუნქციას, სადაც გადაცემულ მონაცემებს  ვწერ ბაზაში
b = int(input("გსურთ ახალი ჩანაწერის დაამატება? დიახ:1 არა:ნებისმიერი სხვა სიმბოლო: "))
if b == 1:
    year = int(input("შემოიტანეთ წელი: "))
    age = int(input("შემოიტანეთ ასაკი: "))
    name = input("შემოიტანეთ მსახიობის სახელი და გვარი: ")
    gender = input("შემოიტანეთ მსახიობის სქესი: ")
    movie = input(f"შემოიტანეთ იმ ფილმის დასახელება, რომელშიც {name}-მა ოსკარი აიღო: ")
    add_record(year, age, name, gender, movie)
get_all_records()

# ამოცანა 4
# მომხმარებელს ვეკითხები სურს თუ არა ცხრილში არსებულ ჩანაწერში ცვლილების განხორციელება და დადასტურების
# შემთხვევაში (თუ 1-იანი შეიყვანა) პროგრამა მოითხოვს იმ ჩანაწერის id-ის შეყვანას, რომელშიც მომხმარებელს სურს
# ცვლილების განხორციელება. ამის შემდეგ  ვკითხულობ მის მიერ შეყვანილ მონაცემებს და გადავცემ update_record ფუნქციას,
# სადაც გადაცემულ მონაცემებს შესაბამისი id-ის მიხედვით  ვწერ ბაზაში. იმ შემთხვევეში თუ მომხმარებელს არ სურს რაიმე ველის
# ცვლილება, უნდა შეიყვანოს იგივე მნიშვნელობა რაც მას აქვს.
b = int(input("გსურთ რაიმე ჩანაწერის შეხვლა? დიახ:1 არა:ნებისმიერი სხვა სიმბოლო: "))
if b == 1:
    id = int(input("რომელი ჩანაწერის შეცვალა გსურთ? (შეომიტანეთ id) "))
    year = int(input("შემოიტანეთ ახალი წელი: "))
    age = int(input("შემოიტანეთ ახალი ასაკი: "))
    name = input("შემოიტანეთ  მსახიობის ახალი სახელი და გვარი: ")
    gender = input("შემოიტანეთ მსახიობის ახალი სქესი: ")
    movie = input(f"შემოიტანეთ იმ ახალი ფილმის დასახელება, რომელშიც {name}-მა ოსკარი აიღო: ")
    update_record(id, year, age, name, gender, movie)
    cur.execute("select * from oscar where id=?", (id,))
conn.close()
plt.show()


