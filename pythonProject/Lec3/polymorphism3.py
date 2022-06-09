class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name: {self.name}; deposit {self.deposit}; loan {self.loan};"


class House:
    def __init__(self, id, price, owner, status):
        self.id = id
        self.price = price
        self.owner = owner
        self.status = status

    def __str__(self):
        return f"id {self.id} price {self.price} owner {self.owner} status {self.status}"

    def sell(self, buyer, money=None):
        self.owner.deposit += self.price
        self.owner = buyer
        if money is None:
            self.status = "gakiduli"
            print("sell with successfully!")
        else:
            self.status = "gakidulia seskhit"
            buyer.loan += money
            print("sell with loan successfully!")


p1 = Person("ekaterine1", 1000, 0)
p2 = Person("ekaterine2", 700, 0)
p3 = Person("ekaterine3", 500, 100)
h1 = House(1, 500, p1, "gasakidi")
h1.sell(p2)
print(p1)
print(p2)
print(h1)

h1.sell(p3, 90)
print(p2)
print(p3)
print(h1)




