from math import inf
import random

class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
    
class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
        print(f"Учитель обучил ученика: {info}")

class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
    def self_learn(self, info):
        self.knowledge.append(info)
        print(f"Ученик выучил: {info}")
    def forget(self):
        forgotten = random.choice(self.knowledge)
        self.knowledge.remove(forgotten)
        print(f"Ученик забыл: {forgotten}")

data = Data("Математика", "Информатика")

teacher = Teacher()
student = Pupil()

teacher.teach(data[0], student)
student.self_learn(data[1])

student.forget()

print("Ученик знает: ", student.knowledge)