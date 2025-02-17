"""Данный модуль содержит классы для рассчёта площади оклеиваемой поверхности
и необходимого количества рулонов обоев."""

class WinDoor:
    """Класс для определения размеров неоклеиваемой поверхности.
    Принимает данные о ширине и длине для находения площади."""
    def __init__(self, w, h):
        self.square = w * h

class Room:
    """Класс для определения комнаты."""
    """Принимает данные о размерах комнаты: ширина, длина, высота."""
    def __init__(self, width, lenght, height):
        self.width = width
        self.lenght = lenght
        self.height = height
        self.wd = []
    """Добавляет площадь неоклеиваемой поверхности WinDoor в список"""
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    """Рассчитывает полную площадь стен комнаты и возвращает результат"""
    def full_square(self):
        return 2 * self.height * (self.length + self.width)
    """Вычисляет конечную площадь стен, которые нужно поклеить."""
    def workSurface(self):
        new_square = self.full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square
    """Вычисляет размер одного рулона обоев и рассчитывает их необходимое количество"""
    def rolls_need(self, roll_w, roll_l):
        roll_square = roll_w * roll_l
        work_square = self.workSurface()
        return work_square / roll_square