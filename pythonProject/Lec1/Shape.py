class Shape:
    def __init__(self, color):
        self.color = color

    def say_hi(self):
        print(f'I am a shape with {self.color} color')


class Quadrangle(Shape):

    def __init__(self, a, b, c, d, color):
        super().__init__(color)
        self.a, self.b, self.c, self.d = a, b, c, d

    def say_hi(self):
        print(f'I am a quadrangle with {self.color} color')


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def say_hi(self):
        print(f"i am a triangle with {self.color} color")


class Rectangle(Quadrangle):
    def __init__(self, a, b, color):
        Shape.__init__(self, color)
        self.a = a
        self.b = b


s1 = Shape('red')
s1.say_hi()
q1 = Quadrangle(4, 2, 1, 6, 'blue')
q1.say_hi()
r1 = Rectangle(1, 5, 'black')
r1.say_hi()
t1 = Triangle(1, 2, 3, "white")
t1.say_hi()
