from math import *

def func(x):
    if -3 <= x <= 6:
        if x < -1:
            return -x - 2
        elif x < 0:
            return sqrt(1 - x**2) + 1
        elif x <= 2:
            return -sqrt(4 - x**2) + 2
        elif x < 4:
            return -1
        else:
            return 0.5 * x - 3
    print("х за пределами числового интервала!")
    return 0

try:
    xf = float(input("Введите начальное х: "))
    xe = float(input("Введите конечное х: "))
    dx = float(input("Введите интервал х: "))

    print(*([f"\t{"-" * 25}\n"] + [f"\t| x = {(xf + dx * x):5.2f} | y = {func(xf + dx * x):5.2f} |\n\t{"-" * 25}\n" for x in range(int((xe - xf) / dx) + 1)]))


except ValueError:
    print("Ошибка типа х!")