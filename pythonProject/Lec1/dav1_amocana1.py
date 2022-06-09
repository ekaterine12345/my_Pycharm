class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
        return "perimeter {}".format(2*(self.width+self.length))

    def area(self):
        return "area {}".format(self.width*self.length)        

    def __str__(self):
        return "width={}, length={}, color={}; ".format(self.width, self.length, self.color)


rec = Rectangle(3, 5, "RED")
print(rec)
print(rec.perimeter())
print(rec.area())
