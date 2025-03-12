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
            try:
                start = float(input("Введите начало интервала: "))
                end = float(input("Введите конец интервала: "))
                segment = LineSegment(start, end)
                collection.add(segment)
            except ValueError as e:
                print(f"Ошибка: {e}")
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