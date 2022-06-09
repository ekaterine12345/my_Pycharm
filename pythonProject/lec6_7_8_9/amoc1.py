class Health:
    def __init__(self, age, gender, puls):
        self.age = age
        self.gender = gender
        self.puls = puls

    def __str__(self):
        return f"age {self.age}, gender {self.gender}, puls {self.puls}"

    def avg_life(self):
        return 2600000000/(self.puls*527040)

    def max_puls(self):
        if self.gender == 'F':
            return 226-0.9*self.age
        elif self.gender == 'M':
            return 223-0.9*self.age

    def max_puls_train(self, train):
        if train == "ინტენსიური მოვარჯიშე":
            factor = 0.8
        if train == "საშუალო დატვირთვა":
            factor = 0.6
        if train == "დამწყები მოვარჯიშე":
            factor = 0.5

        max_beats = Health.max_puls(self)
        return (max_beats-self.puls)*factor+self.puls


h = Health(22, 'F', 80)
print(h)
print(h.avg_life())
print(h.max_puls())
print(h.max_puls_train("ინტენსიური მოვარჯიშე"))
print(h.max_puls_train("საშუალო დატვირთვა"))
print(h.max_puls_train("დამწყები მოვარჯიშე"))
