class WinDoor:
    def __init__(self, w, h):
        self.square = w * h

class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.lenght = length
        self.height = height
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    def full_square(self):
        return 2 * self.height * (self.lenght + self.width)
    def workSurface(self):
        new_square = self.full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square
    def rools_need(self, roll_w, roll_l):
        roll_square = roll_w * roll_l
        work_square = self.workSurface()
        return work_square / roll_square
    
width = float(input("Введите ширину комнаты: "))
length = float(input("Введите длину комнаты: "))
height = float(input("Введите высоту комнаты: "))

room = Room(width, length, height)

flag = input("Есть ли неоклеиваемая поверхность? (1 - да, 2 - нет) ")
while flag == '1':
    w = float(input("Ширина - "))
    h = float(input("Высота - "))
    room.addWD(w, h)
    flag = input("Добавить ещё? (1 - да, 2 - нет)")

print("Введите размеры рулона обоев: ")
roll_w = float(input("Ширина - "))
roll_l = float(input("Длина - "))

print(f"Оклеиваемая площадь: {room.workSurface():.2f}")
print(f"Необходимое количество рулонов: {room.rools_need(roll_w, roll_l):.2f}")