class Service:
    def __init__(self, ser_name, cost, tip, people):
        self.ser_name = ser_name
        self.cost = cost
        self.tip = tip
        self.people = people

    def __str__(self):
        return f"service name: {self.ser_name}, cost: {self.cost}, tip: {self.tip}, people: {self.people} "

    def fun1(self):
        return self.cost+self.cost*self.tip/100

    def fun2(self):
        return Service.fun1(self)/self.people

    def __le__(self, other):
        a1 = Service.fun2(self)
        a2 = Service.fun2(other)
        print(a1, a2)
        return a1 <= a2


s = Service("sern1", 30, 5, 10)
print(s)
print(s.fun1())
print(s.fun2())

s2 = Service("sern2", 29, 10, 10)
print(s2)
print(s2.fun1())
print(s2.fun2())
print(s <= s2)