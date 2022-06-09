class Book:
    def __init__(self, title, price, amount=1):
        self.__title = title
        self.__price = price
        self.__amount = amount

    def __str__(self):
        return f"title {self.__title} price {self.__price} amount {self.__amount}"

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    title1 = property(get_title, set_title)

    def buy(self, amount1):
        if self.__amount >= amount1:
            print(f"you successfully buy {amount1} books")
            self.__amount -= amount1
        else:
            print("amdeni araa")


b = Book("bb", 3, 5)
print(b)
b.title1 = "m"
print(b.title1)
b.buy(4)
