# Неделя 2
## **Тема**: Объектно-ориентированное программирование на Python 
### Студентки группы ПИЖ-б-о-23-1(1) Алдабаевой Виктории Владимировны
#### Репозиторий Git: https://github.com/Pharrower/pizh2311_Aldabaeva <br><br>
**Номер варианта: 2**  
*Задание:*  
Класс "Прямоугольный треугольник"
Класс содержит два действительных числа - стороны треугольника. Включает следующие методы:
- увеличение/уменьшение размера стороны на заданное количество процентов;
- вычисление радиуса описанной окружности;
- вычисление периметра;
- определение значений углов. 

*Ответ:*  
```python
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

# Класс для композиции (содержит список треугольников)
class TriangleCollection:
    def __init__(self):
        self._triangles = []  # Список для хранения треугольников (композиция)

    def add_triangle(self, triangle):
        # Добавляет треугольник в коллекцию
        self._triangles.append(triangle)

    def print_all_triangles(self):
        # Выводит информацию о всех треугольниках в коллекции
        print("Коллекция треугольников:")
        for triangle in self._triangles:
            print(triangle)

# Пример использования
triangle1 = Triangle(3, 4, 5)
triangle2 = RightTriangle(6, 8)

# Создаём коллекцию и добавляем треугольники
collection = TriangleCollection()
collection.add_triangle(triangle1)
collection.add_triangle(triangle2)

# Выводим информацию о всех треугольниках в коллекции
collection.print_all_triangles()
```  
*Вывод программы:*  
Коллекция треугольников:
Треугольник со сторонами: 3, 4, 5
Прямоугольный треугольник с катетами: 6, 8 и гипотенузой: 10.0
