import json

class LineSegment:
    """
    Класс, представляющий математический интервал (отрезок) на числовой прямой.

    Атрибуты:
        start (float): Начало интервала.
        end (float): Конец интервала.
    """

    def __init__(self, start, end):
        """
        Инициализация объекта LineSegment.

        Параметры:
            start (float): Начало интервала.
            end (float): Конец интервала.

        Исключения:
            ValueError: Если start > end.
        """
        if start > end:
            raise ValueError("Начало интервала не может быть больше конца.")
        self.start = start
        self.end = end

    def __str__(self):
        """
        Возвращает строковое представление интервала.

        Возвращаемое значение:
            str: Строка в формате "Интервал(start, end)".
        """
        return f"Интервал({self.start}, {self.end})"

    def __add__(self, other):
        """
        Перегрузка оператора сложения. Объединяет два интервала.

        Параметры:
            other (LineSegment): Другой интервал для объединения.

        Возвращаемое значение:
            LineSegment: Новый интервал, охватывающий оба исходных.
        """
        return LineSegment(min(self.start, other.start), max(self.end, other.end))

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания. Находит пересечение двух интервалов.

        Параметры:
            other (LineSegment): Другой интервал для нахождения пересечения.

        Возвращаемое значение:
            LineSegment: Новый интервал, представляющий пересечение.
            None: Если пересечения нет.
        """
        new_start = max(self.start, other.start)
        new_end = min(self.end, other.end)
        if new_start > new_end:
            return None  # Нет пересечения
        return LineSegment(new_start, new_end)

    def length(self):
        """
        Вычисляет длину интервала.

        Возвращаемое значение:
            float: Длина интервала.
        """
        return self.end - self.start

    def contains(self, value):
        """
        Проверяет, содержится ли значение в интервале.

        Параметры:
            value (float): Значение для проверки.

        Возвращаемое значение:
            str: Да или нет
        """
        if self.start <= value <= self.end:
            print(f"Да, значение {value} содержится в данном интервале")
        else:
            print(f"Нет, значение {value} не содержится в данном интервале")

    def save(self, filename):
        """
        Сохраняет интервал в JSON-файл.

        Параметры:
            filename (str): Имя файла для сохранения.
        """
        data = {'start': self.start, 'end': self.end}
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load(self, filename):
        """
        Загружает интервал из JSON-файла.

        Параметры:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        self.start = data['start']
        self.end = data['end']