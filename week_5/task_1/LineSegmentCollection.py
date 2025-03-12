import json
from LineSegment import LineSegment

class LineSegmentCollection:
    """
    Класс-контейнер для хранения объектов LineSegment.
    """

    def __init__(self):
        """
        Инициализация контейнера.
        """
        self._data = []

    def __str__(self):
        """
        Возвращает строковое представление контейнера.
        """
        return "\n".join(f"{i}: {segment}" for i, segment in enumerate(self._data))

    def __getitem__(self, index):
        """
        Возвращает элемент контейнера по индексу.
        """
        return self._data[index]

    def add(self, segment):
        """
        Добавляет объект LineSegment в контейнер.

        Параметры:
            segment (LineSegment): Объект LineSegment для добавления.
        """
        self._data.append(segment)
        print(f"{segment} добавлен в коллекцию.")

    def remove(self, index):
        """
        Удаляет объект LineSegment из контейнера по индексу.

        Параметры:
            index (int): Индекс элемента для удаления.
        """
        if 0 <= index < len(self._data):
            removed_segment = self._data.pop(index)
            print(f"{removed_segment} удален из коллекции.")
        else:
            print("Ошибка: Интервала с таким индексом не существует.")

    def save(self, filename):
        """
        Сохраняет контейнер в JSON-файл.

        Параметры:
            filename (str): Имя файла для сохранения.
        """
        data = [{'start': segment.start, 'end': segment.end} for segment in self._data]
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Коллекция сохранена в файл {filename}.")

    def load(self, filename):
        """
        Загружает контейнер из JSON-файла.

        Параметры:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        self._data = [LineSegment(segment['start'], segment['end']) for segment in data]
        print(f"Коллекция загружена из файла {filename}.")