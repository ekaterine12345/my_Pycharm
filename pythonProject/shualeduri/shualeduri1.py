class Ticket:
    def __init__(self, film_name, price, language="Geo"):
        self.film_name = film_name
        self.price = price
        self.language = language

    def __str__(self):
        return f"film name: {self.film_name}, price: {self.price}, language: {self.language}"


class User:
    def __init__(self, buyer, balance):
        self.buyer = buyer
        self.balance = balance

    def __str__(self):
        return f"buyer: {self.buyer}, balance: {self.balance}"

    def buy(self, ticket, amount):
        if ticket.price*amount <= self.balance:
            self.balance -= ticket.price*amount
            print(f"tqven ikidet {amount} bileti")
        else:
            print("ar gaqvt sakmarisi tanxa")

    def deposit(self, money):
        self.balance += money


t1 = Ticket("film1", 20)
print(t1)

u1 = User("kato", 500)
print(u1)
u1.deposit(300)
print(u1)
u1.buy(t1, 50)
u1.buy(t1, 20)
print(u1)
u1.buy(t1, 25)
print(u1)




