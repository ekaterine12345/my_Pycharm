import math


class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def inverse(self):
        return Fraction(self.bottom, self.top)

    def sum_fractions(self, other):
        b1 = self.bottom
        b2 = other.bottom
        bottom = int(b1*b2/math.gcd(b1, b2))
        return Fraction(int(self.top*bottom/b1 + other.top*bottom/b2), bottom)


fraction1 = Fraction(3, 4)
print(fraction1)
fraction2 = Fraction(7, 6)
print(f"inverse({fraction2}) = ", fraction2.inverse())
print(f"{fraction1} + {fraction2} = ", fraction1.sum_fractions(fraction2))
