class Person:
    def __init__(self, name, surname, prof=1):
        self.name = name
        self.surname = surname
        self.prof = prof

    def info(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Квалификация: {self.prof}"
    
    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}")

person1 = Person("Иван", "Иванов", 1)
person2 = Person("Елизавета", "Евгеньевна", 2)
person3 = Person("Александр", "Смирнов", 3)

print(person1.info())
print(person2.info())
print(person3.info())

if person1.prof < person2.prof and person1.prof < person3.prof:
    del(person1)
elif person2.prof < person1.prof and person2.prof < person3.prof:
    del(person2)
else:
    del(person3)

input("Нажмите Enter для завершения программы")
