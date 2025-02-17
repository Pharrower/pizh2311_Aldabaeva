from module import WinDoor, Room

width = float(input("Введите ширину комнаты: "))
length = float(input("Введите длину комнаты: "))
height = float(input("Введите высоту комнаты: "))

room = Room(width, length, height)

flag = input("Есть ли неоклеиваемая поверхность? (1 - да, 2 - нет) ")
while flag == '1':
    w = float(input("Ширина - "))
    h = float(input("Высота - "))
    room.addWD(w, h)
    flag = input("Добавить ещё? (1 - да, 2 - нет) ")

print("Введите размеры рулона обоев: ")
roll_w = float(input("Ширина - "))
roll_l = float(input("Длина - "))

print(f"Оклеиваемая площадь: {room.workSurface():.2f}")
print(f"Необходимое количество рулонов: {room.rolls_need(roll_w, roll_l):.2f}")