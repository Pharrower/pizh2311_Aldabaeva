from ПишущиеПринадлежности import ПишущаяПринадлежность
from ПишущиеПринадлежности import Карандаш
from ПишущиеПринадлежности import Ручка
from ПишущиеПринадлежности import ГелеваяРучка

def main():
    print("Создание пишущих принадлежностей:")
    
    # Ввод данных для карандаша
    print("\nСоздание карандаша:")
    цвет_карандаша = input("Введите цвет карандаша: ")
    толщина_карандаша = float(input("Введите толщину линии карандаша: "))
    твердость_грифеля = input("Введите твердость грифеля (например, HB, 2B): ")
    
    карандаш = Карандаш(цвет_карандаша, толщина_карандаша, твердость_грифеля)
    
    # Ввод данных для ручки
    print("\nСоздание ручки:")
    цвет_ручки = input("Введите цвет ручки: ")
    толщина_ручки = float(input("Введите толщину линии ручки: "))
    тип_ручки = input("Введите тип ручки (например, шариковая, гелевая): ")
    
    ручка = Ручка(цвет_ручки, толщина_ручки, тип_ручки)
    
    # Ввод данных для гелевой ручки
    print("\nСоздание гелевой ручки:")
    цвет_гелевой_ручки = input("Введите цвет гелевой ручки: ")
    толщина_гелевой_ручки = float(input("Введите толщину линии гелевой ручки: "))
    материал_корпуса = input("Введите материал корпуса ручки (например, алюминий, пластик): ")
    
    гелевая_ручка = ГелеваяРучка(цвет_гелевой_ручки, толщина_гелевой_ручки, тип_ручки, материал_корпуса)
    
    # Демонстрация работы методов
    print("\nРезультаты:")
    print("Карандаш:")
    карандаш.писать()
    
    print("\nРучка:")
    ручка.писать()
    
    print("\nГелевая ручка:")
    гелевая_ручка.писать()

if __name__ == "__main__":
    main()

    #Пример вывода:

#Создание пишущих принадлежностей:

#Создание карандаша:     
#Введите цвет карандаша: чёрный
#Введите толщину линии карандаша: 0.7
#Введите твердость грифеля (например, HB, 2B): B

#Создание ручки:     
#Введите цвет ручки: красный
#Введите толщину линии ручки: 0.2
#Введите тип ручки (например, шариковая, гелевая): шариковая

#Создание гелевой ручки:     
#Введите цвет гелевой ручки: синий
#Введите толщину линии гелевой ручки: 0.4
#Введите материал корпуса ручки: (например: алюминий, пластик) пластик

#Результаты:
#Карандаш:
#Карандаш пишет цветом: чёрный, толщина линии: 0.7, твёрдость грифеля: B

#Ручка:
#Ручка пишет цветом: красный, толщина линии: 0.2, тип ручки: шариковая.

#Гелевая ручка:
#Тип ручки: Гелевая, ручка пишет цветом: синий, толщина линии: 0.4, материал корпуса: пластик.