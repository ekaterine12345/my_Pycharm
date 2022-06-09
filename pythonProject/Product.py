class Product:
    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def get_name(self):
        return self.__name

    def set_name(self, n1):
        self.__name = n1

    def get_price(self):
        return self.__price

    def set_price(self, p1):
        self.__price = p1

    def get_amount(self):
        return self.__amount

    def set_amount(self, a1):
        self.__amount = a1

    def print_info(self):
        print(f"name: {self.__name}, price: {self.__price}, amount: {self.__amount}")

    def __gt__(self, other):
        return self.__amount > other.__amount

    def __lt__(self, other):
        return self.__amount < other.__amount


class Apple(Product):
    def __init__(self, name, price, amount, variety):
        super().__init__(name, price, amount)
        self.__variety = variety


a1 = Apple('app', 5, 10, 'Antonovka')
a1.print_info()
a1.set_name('app2')
a1.set_price(12)
a1.set_amount(15)

a2 = Apple('app5', 5, 11, 'Antonovka')
a2.set_amount(4)
a2.print_info()

print(a1.get_name(), a1.get_price(), a1.get_amount())
print(a1 > a2)
print(a1 < a2)

