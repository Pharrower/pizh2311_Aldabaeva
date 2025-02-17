import math

class Triangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def change_sides(self, side, percent):
        if side == 1:
            self.side1 *= (1 + percent / 100)
        else:
            self.side2 *= (1 + percent / 100)

    def radius(self):
        radius = math.sqrt(self.side1**2 + self.side2**2) / 2
        return radius
    
    def perimeter(self):
        perimeter = math.sqrt(self.side1**2 + self.side2**2) / 2 + self.side1 + self.side2
        return perimeter
    
    def corners(self):
        corner1 = 90
        corner2 =  math.degrees(math.atan(self.side1 / self.side2))
        corner3 = corner1 - corner2
        return corner1, corner2, corner3
    
triangle = Triangle(3, 4)
print("Периметр треуольника: ", triangle.perimeter())
print("Радиус описанной окружности: ", triangle.radius())
print("Углы треугольника: ", triangle.corners())

triangle.change_sides(1, 10)
print("Изменение первого катета: ", triangle.side1)
