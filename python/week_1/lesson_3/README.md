# Урок 3. Конструктор класса - метод __init__()

1. Есть класс персон, конструктор котороо принимает три параметра (не учитывая self) - имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.
2. У класса Person есть метод, который возвращает строку включающую в себя всю информацию о сотруднике.
3. Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер ..." (вместо троеточия должны выводиться имя и фамилия объекта).
4. В основной ветке прораммы создайте три объекта классна Person. Посмотрите информацию о сотрудниках и увольте самое слабое звено.
5. В конце прораммы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет нажат Enter. Иначе вы сразу увидите, как удаляются все объекты при завершении работы программы.