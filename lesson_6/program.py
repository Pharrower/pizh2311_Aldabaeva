class Number:
    def __init__(self, a):
        self.__a = Number.__check(a)
    def setA(self, a):
        self.__a = Number.__check(a)
        print(f"Вы задали новое значение: a = {self.__a}")
    def getA(self):
        return f"Число а = {self.__a}"
    def __check(value):
        if value < 0:
            return abs(value)
        else:
            return value
    def __str__(self):
        return f"Число a = {self.__a}"
    
a = Number(3)
print(a.getA())
a.setA(5)
print(a.getA())