class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}.uni@btu.edu.ge"

    def __str__(self):
        return f"Email: {Person.get_email(self)}"


class Lecturer(Person):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@btu.edu.ge"

    def __str__(self):
        return f"Email : {Lecturer.get_email(self)}   Salary : {self.salary} "


class Student(Person):
    def __init__(self, firstname, lastname, courses=[]):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_email(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}.1@btu.edu.ge"

    def __str__(self):
        return f"Email: {Student.get_email(self)}   Courses: {self.courses} "


p1 = Person("Kato", "Gurgenidze")
print(p1)

l1 = Lecturer("Lika", "Svanadze", 10000000)
print(l1)

s1 = Student("Ekaterine", "Gurgenidze", ["python", "Calculus", "management", "Oracle", "computer architecture",
                                         "Startup"])
print(s1)
