class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def __str__(self):
        return f"{self.age} old, {self.size.lower()}, {self.color.lower()} {self.breed}"

    def eat(self):
        return f"{self} is eating"

    def sleep(self):
        return f"{self} in sleeping"

    def sit(self):
        return f"{self} is sitting"

    def run(self):
        return f"{self} is running"   


def fun(dog):
    print(dog.eat())
    print(dog.sleep())
    print(dog.sit())
    print(dog.run())
    print("\n")


dog1 = Dog("Neapolitan Mastiff", "Large", "5 years", "Black")
fun(dog1)

dog2 = Dog("Maltese", "Small", "2 years", "White")
fun(dog2)

dog3 = Dog("Chow Chow", "Medium", "3 years", "Brown")
fun(dog3)
