class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, temperature):
        self.__temperature = temperature

    def del_temp(self):
        del self.__temperature

    temp = property(get_temp, set_temp, del_temp)


celsius1 = Celsius(50)
print(celsius1.temp)    
celsius1.temp = 30
print(celsius1.temp)    
del celsius1.temp
# print(celsius1.temp)

celsius2 = Celsius(5)
print(celsius2.temp)    
celsius2.temp = 100
print(celsius2.temp)    
del celsius2.temp
# print(celsius2.temp)
