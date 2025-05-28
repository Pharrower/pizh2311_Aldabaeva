class WinDoor:
    def __init__(self, w, h):
        self.square = w * h

class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.wd = []

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))

    def full_square(self):
        return 2 * self.height * (self.length + self.width)

    def workSurface(self):
        new_square = self.full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def rolls_need(self, roll_w, roll_l):
        roll_square = roll_w * roll_l
        work_square = self.workSurface()
        return work_square / roll_square