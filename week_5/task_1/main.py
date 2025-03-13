from LineSegment import LineSegment
from LineSegmentCollection import LineSegmentCollection

def display_menu():
    """
    Отображает меню для пользователя.
    """
    print("\nМеню:")
    print("1. Просмотреть коллекцию")
    print("2. Добавить интервал")
    print("3. Удалить интервал")
    print("4. Сохранить коллекцию в файл")
    print("5. Загрузить коллекцию из файла")
    print("6. Выйти")

def main():
    collection = LineSegmentCollection()

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nТекущая коллекция интервалов:")
            print(collection)
        elif choice == '2':
            start = float(input("Введите начало интервала: "))
            end = float(input("Введите конец интервала: "))
            segment = LineSegment(start, end)
            collection.add(segment)
        elif choice == '3':
            try:
                index = int(input("Введите индекс интервала для удаления: "))
                collection.remove(index)
            except ValueError:
                print("Ошибка: Введите корректный индекс.")
        elif choice == '4':
            filename = input("Введите имя файла для сохранения: ")
            if filename.find('.json') == -1:
                filename += '.json'
            collection.save(filename)
        elif choice == '5':
            filename = input("Введите имя файла для загрузки: ")
            collection.load(filename)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")

if __name__ == "__main__":
    main()

# Пример вывода:

#Меню:
#1. Просмотреть коллекцию       
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл  
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 2
#Введите начало интервала: 1
#Введите конец интервала: 5
#Интервал(1.0, 5.0) добавлен в коллекцию.

#Меню:
#1. Просмотреть коллекцию
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 2
#Введите начало интервала: 3
#Введите конец интервала: 7
#Интервал(3.0, 7.0) добавлен в коллекцию.

#Меню:
#1. Просмотреть коллекцию
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 1

#Текущая коллекция интервалов:
#0: Интервал(1.0, 5.0)
#1: Интервал(3.0, 7.0)

#Меню:
#1. Просмотреть коллекцию
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 3
#Введите индекс интервала для удаления: 0
#Интервал(1.0, 5.0) удален из коллекции.

#Меню:
#1. Просмотреть коллекцию
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 4
#Введите имя файла для сохранения: collection
#Коллекция сохранена в файл collection.json.

#Меню:
#1. Просмотреть коллекцию
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 5
#Введите имя файла для загрузки: collection.json
#Коллекция загружена из файла collection.json.

#Меню:
#1. Просмотреть коллекцию
#2. Добавить интервал
#3. Удалить интервал
#4. Сохранить коллекцию в файл
#5. Загрузить коллекцию из файла
#6. Выйти
#Выберите действие: 6
#Выход из программы.