from math import *
try:
    x = float(input("Введите x: "))

    if -3 <= x <= 6:
        if x < -1:
            y = -x - 2
        elif x < 0:
            y = sqrt(1 - x**2) + 1
        elif x <= 2:
            y = -sqrt(4 - x**2) + 2
        elif x < 4:
            y = -1
        else:
            y = 0.5 * x - 3
        print(f"y = {y:.2f}")
    else:
        print("х за пределами числового интервала!")

except ValueError:
    print("Ошибка типа х!")