class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def __str__(self):
        return f"width={self.width}, length={self.length}, color={self.color}; "

    def perimeter(self):
        return f"perimeter {2*(self.width+self.length)}"

    def area(self):
        return f"area {self.width*self.length}"


rec = Rectangle(3, 5, "RED")
print(rec)
print(rec.perimeter())
print(rec.area())
