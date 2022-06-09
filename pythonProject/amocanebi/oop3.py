class Bus:
    def __init__(self, number, price, seat, info=[]):
        self.number = number
        self.price = price
        self.seat = seat
        self.info = info

    def __str__(self):
        return f'ავტობუსის ნომერი: {self.number}, ღირებულება: {self.price},' \
               f' ადგილების რაოდენობა: {self.seat}, ინფორმაცია მგზავრების შესახებ: {self.info}'


class Bus_card:
    def __init__(self, ID, name, balance, history=[]):
        self.id = ID
        self.name = name
        self.balance = balance
        self.history = history

    def __str__(self):
        return f'ID: {self.id}, passenger name: {self.name}, ' \
               f'balance: {self.balance}, history: {self.history}'

    def add_pes(self, other):
        if isinstance(other, Bus):
            self.balance -= other.price
            self.history.append(other.__str__())
            other.info.append(self.name)
        else:
            return 'შეიყვანეთ სწორი მონაცემები'


b1 = Bus(1, 1.5, 15, ['12, 34, 11'])
print(b1)
p1 = Bus_card(1, 'kato', 10, ['nia', 'luka', 'maia'])
print(p1)
p1.add_pes(b1)
print(p1)