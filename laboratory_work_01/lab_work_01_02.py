from math import *

try:
    x = float(input("Введите x: "))
except ValueError:
    print("Ошибка типа для х!")
    x = 0

try:
    tmp11 = x**2 + 2 * x - 3 + (x + 1) * sqrt(x ** 2 - 9)
    tmp12 = x**2 - 2 * x - 3 + (x - 1) * sqrt(x ** 2 - 9)
    z1 = tmp11 / tmp12
except ValueError, ZeroDivisionError:
    print("Деление на 0!")
    z1 = 0
print("x = {:.2f} z1 = {:.4f}".format(x, z1))

try:
    tmp21 = (x + 3) / (x - 3)
    z2 = sqrt(tmp21)
except ValueError, ZeroDivisionError:
    print("Деление на 0!")
    z2 = 0
print("x = {0:.2f} z2 = {1:.4f}".format(x, z2))
