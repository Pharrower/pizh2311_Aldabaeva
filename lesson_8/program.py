class Snow:
    def __init__(self, snowflakes):
        self.snowflakes = snowflakes

    def __call__(self, new_snowflakes):
        self.snowflakes = new_snowflakes

    def __add__(self, n):
        return Snow(self.snowflakes + n)
    
    def __sub__(self, n):
        return Snow(self.snowflakes - n)
    
    def __mul__(self, n):
        return Snow(self.snowflakes * n)
    
    def __truediv__(self, n):
        return Snow(round(self.snowflakes / n))
    
    def makeSnow(self, snowflakes_row):
        rows = self.snowflakes // snowflakes_row
        ost = self.snowflakes % snowflakes_row
        s = ''
        for _ in range(rows):
            s = s + '*' * snowflakes_row + '\n'
        if ost > 0:
            s = s + '*' * ost
        return s

snow = Snow(int(input("Введите изначальное кол-во снежинок: ")))

snow = snow + int(input("Сколько снежинок прибавить: "))
snow = snow - int(input("Сколько снежинок вычесть: "))
snow = snow * int(input("Во сколько раз умножить снежинки: "))
snow = snow / int(input("Во сколько раз сократить кол-во снежинок: "))

n = int(input("Введите кол-во снежнок в ряду: "))
print("Cнежинки!")
print(snow.makeSnow(n))