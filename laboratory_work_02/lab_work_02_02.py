from math import *

try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    # y = -x**2 + 2 y = 0.5x x = -sqrt(-y + 2) x = 2y
    if y <= 0 and -sqrt(-y + 2) <= 2 * y:
        print("Попал!")
    elif y > 0 and 2 * y <= sqrt(-y + 2):
        print("Попал!")
    else:
        print("Не попал!")   

except ValueError:
    print("Ошибка")

