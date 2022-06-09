class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}.uni@btu.edu.ge"


class Lecturer(Person):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@btu.edu.ge"


class Student(Person):
    def __init__(self, firstname, lastname, courses=[]):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}.1@btu.edu.ge"


class DoctoralStudent(Lecturer, Student):
    def __init__(self, firstname, lastname, salary, courses=[]):
        super().__init__(firstname, lastname, salary)
        Student.__init__(self, firstname, lastname, courses)

    def get_email(self):
        return Student.get_email(self), super().get_email()

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.salary} {self.courses}"


p1 = Person("Kato", "Gurgenidze")
print(p1.get_email())

l1 = Lecturer("Lika", "Svanadze", 10000000)
print(l1.get_email())

s1 = Student("Ekaterine", "Gurgenidze", ["python", "Calculus", "management", "Oracle", "computer architecture",
                                         "Startup"])
print(s1.get_email())

d1 = DoctoralStudent("Ekaterine2", "Gurgenidze2", 10000, ["python2", "Calculus2", "management", "Oracle Database",
                                                          "computer architecture", "Startup"])
print(d1.get_email())
