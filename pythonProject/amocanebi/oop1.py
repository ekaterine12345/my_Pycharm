class illness:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return f'ID: {self.id}, title: {self.title}'


class Doctor:
    def __init__(self, name, department, patients=[]):
        self.name = name
        self.department = department
        self.patients = patients

    def __str__(self):
        return f'name: {self.name}, department: {self.department}, patients: {self.patients}'


class Patient:
    def __init__(self, id, name, other, illness_name=[]):
        self.id = id
        self.name = name
        self.doctor = other.name
        self.illness = illness_name

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, doctor: {self.doctor}, illness: {self.illness}'

    def diagnose(self, other_illness, other_doctor=None):
        if other_doctor is not None:
            self.illness.append(other_illness.title)
            if len(other_doctor.patients) < 20:
                self.doctor = other_doctor.name
                other_doctor.patients.append(self.name)
            else:
                return 'მიმაგრება ვერ მოხერხდა'
        else:
            self.illness.append(other_illness.title)
            self.doctor = 'ექიმი არ არსებობს'


i1 = illness(1, 'covid-19')
print(i1)
d1 = Doctor('nino', 'virus', ['salome', 'giorgi'])
d2 = Doctor('lika', 'director', [])
print(d1)
p1 = Patient(223455, 'vano', d1, ['virus'])
print(p1)
p1.diagnose(i1, d2)
print(p1)
print(d2)
