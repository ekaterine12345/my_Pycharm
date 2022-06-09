import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance(self, other):
        return f"distance between {self} and {other} is {math.sqrt( (other.x-self.x)**2 + (other.y-self.y)**2 )}"

    def __sub__(self, other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1, point2)
print(point1.distance(point2))
print(point2-point1)
print(point1+point2+point1)
