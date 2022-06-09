class Vocation:
    def __init__(self, name, cost, amount=10):
        self.__name = name
        self.__cost = cost
        self.__amount = amount

    def __str__(self):
        return f"tour name: {self.__name}  tour cost: {self.__cost} left: {self.__amount}"

    def get_name(self):
        return self.__name

    def set_name(self, n1):
        self.__name = n1

    name1 = property(get_name, set_name)

    def booking(self, amount1):
        if self.__amount >= amount1:
            self.__amount -= amount1
            return f"booking {amount1} places with success!"
        else:
            return "not enough places"


v1 = Vocation("bb", 5, 11)
print(v1)
v1.name1 = "mnmnmn"
print(v1.name1)
print(v1.booking(9))
print(v1.booking(3))



