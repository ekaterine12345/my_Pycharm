class Car:
    def __init__(self, color, model, makeYear, fuelType):
        self.color = color
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType

    def __str__(self):
        return f"color={self.color}, model={self.model}, makeYear={self.makeYear}, fuelType={self.fuelType};"

    def sell(self):
        return "sell car {}".format(self)

    def buy(self):
        return "buy car {}".format(self)

    def rent(self):
        return "rent car {}".format(self)

    def insurance(self):
        return "insurance car {}".format(self)    


def fun(car):
    print(car.sell())
    print(car.buy())
    print(car.rent())
    print(car.insurance())
    print("\n")


car1 = Car("red", "Mercedes", 2015, "Gas")
fun(car1)

car2 = Car("blue", "BMW", 2013, "Gas")
fun(car2)

car3 = Car("orange", "Audi", 2009, "Diesel")
fun(car3)
