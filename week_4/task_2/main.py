from math import pi
from LineSegment import LineSegment

def main():
    # Ввод первого интервала
    start1, end1 = map(float, input("Введите первый интервал в формате 'start,end': ").split(','))
    segment1 = LineSegment(start1, end1)

    # Ввод второго интервала
    start2, end2 = map(float, input("Введите первый интервал в формате 'start,end': ").split(','))
    segment2 = LineSegment(start2, end2)

    # Вывод информации о интервалах
    print("\nВведенные интервалы:")
    print("Интервал 1:", segment1)
    print("Интервал 2:", segment2)

    # Операции с интервалами
    sum_segment = segment1 + segment2
    diff_segment = segment1 - segment2

    print("\nРезультаты операций:")
    print("Сумма интервалов:", sum_segment)
    print("Пересечение интервалов:", diff_segment)

    # Длина интервалов
    print("\nДлины интервалов:")
    print("Длина интервала 1:", segment1.length())
    print("Длина интервала 2:", segment2.length())

    # Проверка на содержание значения
    value = float(input("\nВведите значение для проверки в интервале 1: "))
    print("Интервал 1: ")
    segment1.contains(value)
    print("Интервал 2:")
    segment2.contains(value)

    # Сохранение и загрузка интервала
    save_option = input("\nХотите сохранить интервал 1 в файл? (да/нет): ").lower()
    if save_option == 'да':
        filename = input("Введите имя файла для сохранения: ")
        if filename.find('.json') == -1:
            filename += '.json'
        segment1.save(filename)
        print(f"Интервал 1 сохранен в файл '{filename}'.")

        load_option = input("Хотите загрузить интервал из файла? (да/нет): ").lower()
        if load_option == 'да':
            loaded_segment = LineSegment(0, 0)
            loaded_segment.load(filename)
            print("Загруженный интервал:", loaded_segment)

if __name__ == "__main__":
    main()

# Пример вывода:

#Введите первый интервал в формате 'start,end': 1,5
#Введите первый интервал в формате 'start,end': 3,7

#Введенные интервалы:
#Интервал 1: Интервал(1.0, 5.0)
#Интервал 2: Интервал(3.0, 7.0)

#Результаты операций:
#Сумма интервалов: Интервал(1.0, 7.0)
#Пересечение интервалов: Интервал(3.0, 5.0)

#Длины интервалов:
#Длина интервала 1: 4.0
#Длина интервала 2: 4.0

#Введите значение для проверки в интервале 1: 2
#Интервал 1: 
#Да, значение 2.0 содержится в данном интервале
#Интервал 2:
#Нет, значение 2.0 не содержится в данном интервале

#Хотите сохранить интервал 1 в файл? (да/нет): да
#Введите имя файла для сохранения: file_1
#Интервал 1 сохранен в файл 'file_1.json'.
#Хотите загрузить интервал из файла? (да/нет): да
#Загруженный интервал: Интервал(1.0, 5.0)