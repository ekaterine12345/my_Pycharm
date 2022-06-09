class Currency:

    dict1 = {"GEL": 1, "USD": 2.7, "EUR": 3}

    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{'%.2f' % self.value} {self.unit}"

    def changeTo(self, unit2):
        x = self.value * Currency.dict1[self.unit]

        return Currency(x / Currency.dict1[unit2], unit2)

    def __add__(self, other):
        if isinstance(self, Currency) and isinstance(other, Currency):
            if self.unit != other.unit:
                other = Currency.changeTo(other, self.unit)
            return Currency(self.value + other.value, self.unit)
        elif isinstance(self, Currency):
            return Currency(self.value+other, self.unit)

    def __radd__(self, other):
        return Currency(self.value + other, self.unit)
    
    def __mul__(self, other):
        try:
            return Currency(self.value * other, self.unit)
        except TypeError:
            return "typeerror"

    def __rmul__(self, other):
        return Currency.__mul__(self, other)

    def __gt__(self, other):
        if self.unit != other.unit:
            self = Currency.changeTo(self, other.unit)

        return self.value > other.value


obj1 = Currency(400)
print(obj1)
change_obj1 = obj1.changeTo("USD")
print(change_obj1)
print(change_obj1.changeTo("GEL"))

obj2 = Currency(100, "USD")

obj3 = Currency(200, "EUR")
print(obj2 + obj3)

sum_obj = 100 + obj2 + 100
print(sum_obj)

por_obj = 3 * obj3 * 2
print(por_obj)

print(obj1 > obj2)
