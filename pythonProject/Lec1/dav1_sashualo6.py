import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2+self.y**2)    


point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1.length())
print(point2.length())
