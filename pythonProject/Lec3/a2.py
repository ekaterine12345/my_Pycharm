class Flat:
    def __init__(self, owner, price, id, status="gasakidi"):
        self.__owner = owner
        self.__price = price
        self.__id = id
        self.__status = status

    def __str__(self):
        return f"{self.__owner} {self.__price} {self.__id} {self.__status}"

    def get_id(self):
        return self.__id

    def set_id(self, id1):
        self.__id = id1

    id_property = property(get_id, set_id)


f1 = Flat("sdd", 5, 5, "av")
print(f1.id_property)
f1.id_property = 9
print(f1)

