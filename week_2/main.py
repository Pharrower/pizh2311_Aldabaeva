import math

# Базовый класс Triangle
class Triangle:
    def __init__(self, side1, side2, side3):
        self._side1 = side1  # Защищённый атрибут (инкапсуляция)
        self._side2 = side2  # Защищённый атрибут (инкапсуляция)
        self._side3 = side3  # Защищённый атрибут (инкапсуляция)

    def perimeter(self):
        # Периметр треугольника
        return self._side1 + self._side2 + self._side3

    def __str__(self):
        # Полиморфизм: метод __str__ для базового класса
        return f"Треугольник со сторонами: {self._side1}, {self._side2}, {self._side3}"

# Подкласс RightTriangle (наследует Triangle)
class RightTriangle(Triangle):
    def __init__(self, side1, side2):
        # Наследование: вызываем конструктор базового класса
        # Гипотенуза вычисляется по теореме Пифагора
        super().__init__(side1, side2, math.sqrt(side1**2 + side2**2))

    def perimeter(self):
        # Полиморфизм: переопределяем метод perimeter для прямоугольного треугольника
        return self._side1 + self._side2 + self._side3

    def radius(self):
        # Радиус описанной окружности
        return self._side3 / 2  # Для прямоугольного треугольника R = гипотенуза / 2

    def corners(self):
        # Углы прямоугольного треугольника
        corner1 = 90  # Прямой угол
        corner2 = math.degrees(math.atan(self._side1 / self._side2))  # Угол между side2 и гипотенузой
        corner3 = 90 - corner2  # Третий угол
        return corner1, corner2, corner3

    def __str__(self):
        # Полиморфизм: переопределяем метод __str__ для подкласса
        return f"Прямоугольный треугольник с катетами: {self._side1}, {self._side2} и гипотенузой: {self._side3}"

# Пример использования
triangle = Triangle(3, 4, 5)
print(triangle)
print("Периметр треугольника:", triangle.perimeter())

right_triangle = RightTriangle(3, 4)
print("\n", right_triangle)
print("Периметр прямоугольного треугольника:", right_triangle.perimeter())
print("Радиус описанной окружности:", right_triangle.radius())
print("Углы прямоугольного треугольника:", right_triangle.corners())