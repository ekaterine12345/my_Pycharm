class Cat:
    def eat(self):
        print("Cat eats a milk")

    def talk(self):
        print("Cat says miaww")

    def walk(self):
        print("Cat can run 20km/h")


class Dog:
    def eat(self):
        print("Dog eats a bone")

    def talk(self):
        print("Dog says Aww")

    def walk(self):
        print("Dog can run 40km/h")


c1 = Cat()
d1 = Dog()

animal = (c1, d1)

for obj in animal:
    obj.eat()
    obj.talk()
    obj.walk()
