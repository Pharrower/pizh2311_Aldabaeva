import math
from abc import ABC, abstractmethod
from typing import Literal

# Абстрактный базовый класс Shape
class Shape(ABC):
    """Абстрактный базовый класс для всех фигур."""

    @abstractmethod
    def perimeter(self) -> float:
        """Абстрактный метод для вычисления периметра фигуры."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового представления фигуры."""
        pass

# Базовый класс Triangle (наследует Shape)
class Triangle(Shape):
    """Класс, представляющий простой треугольник."""

    def __init__(self, side1: float, side2: float, side3: float):
        """
        Инициализирует треугольник с тремя сторонами.

        :param side1: Длина первой стороны.
        :param side2: Длина второй стороны.
        :param side3: Длина третьей стороны.
        """
        self._side1 = side1  # Защищённый атрибут (инкапсуляция)
        self._side2 = side2  # Защищённый атрибут (инкапсуляция)
        self._side3 = side3  # Защищённый атрибут (инкапсуляция)

    def perimeter(self) -> float:
        """Вычисляет периметр треугольника.

        :return: Периметр треугольника.
        """
        return self._side1 + self._side2 + self._side3

    def __str__(self) -> str:
        """Возвращает строковое представление треугольника с полной информацией.

        :return: Строка с информацией о сторонах и периметре.
        """
        return (
            f"Треугольник:\n"
            f"  Стороны: {self._side1}, {self._side2}, {self._side3}\n"
            f"  Периметр: {self.perimeter()}"
        )

# Подкласс RightTriangle (наследует Triangle)
class RightTriangle(Triangle):
    """Класс, представляющий прямоугольный треугольник."""

    def __init__(self, side1: float, side2: float):
        """
        Инициализирует прямоугольный треугольник с двумя катетами.

        :param side1: Длина первого катета.
        :param side2: Длина второго катета.
        """

        Triangle.__init__(self, side1, side2, side3 = math.sqrt(side1**2 + side2**2))

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольного треугольника.

        :return: Периметр прямоугольного треугольника.
        """
        return self._side1 + self._side2 + self._side3

    def radius(self) -> float:
        """Вычисляет радиус описанной окружности.

        :return: Радиус описанной окружности.
        """
        return self._side3 / 2

    def corners(self) -> tuple[Literal[90], float, float]:
        """Вычисляет углы прямоугольного треугольника.

        :return: Кортеж из трёх углов треугольника в градусах.
        """
        corner1 = 90  
        corner2 = math.degrees(math.atan(self._side1 / self._side2)) 
        corner3 = 90 - corner2
        return corner1, corner2, corner3

    def __str__(self) -> str:
        """Возвращает строковое представление прямоугольного треугольника с полной информацией.

        :return: Строка с информацией о катетах, гипотенузе, периметре, радиусе и углах.
        """
        return (
            f"Прямоугольный треугольник:\n"
            f"  Катеты: {self._side1}, {self._side2}\n"
            f"  Гипотенуза: {self._side3}\n"
            f"  Периметр: {self.perimeter()}\n"
            f"  Радиус описанной окружности: {self.radius()}\n"
            f"  Углы: {self.corners()}"
        )

# Класс для композиции (содержит список фигур)
class ShapeCollection:
    """Класс для управления коллекцией фигур."""

    def __init__(self):
        """Инициализирует коллекцию фигур."""
        self._shapes: list = []

    def add_shape(self, shape):
        """Добавляет фигуру в коллекцию.

        :param shape: Фигура (объект класса Shape или его подклассов).
        """
        self._shapes.append(shape)

    def print_all_shapes(self):
        """Выводит информацию о всех фигурах в коллекции."""
        print("Список добавленных фигур:")
        for shape in self._shapes:
            print(shape)

# Пример использования
triangle: Triangle = Triangle(3, 4, 5)
right_triangle: RightTriangle = RightTriangle(6, 8)

# Создаём коллекцию и добавляем фигуры
collection: ShapeCollection = ShapeCollection()
collection.add_shape(triangle)
collection.add_shape(right_triangle)

# Выводим информацию о всех фигурах в коллекции
collection.print_all_shapes()

#Результат
#Коллекция фигур:
#Треугольник:
  #Стороны: 3, 4, 5
  #Периметр: 12
#Прямоугольный треугольник:
  #Катеты: 6, 8
  #Гипотенуза: 10.0
  #Периметр: 24.0
  #Радиус описанной окружности: 5.0
  #Углы: (90, 36.86989764584402, 53.13010235415598)