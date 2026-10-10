from math import *
from random import uniform


def func(x, y):
    return [True if y <= 0 and -sqrt(-y + 2) <= 2 * y or y > 0 and 2 * y <= sqrt(-y + 2) else False, x, y]

try:
    
    print(*([f"\t  X       Y     RES\n\t{"-" * 19}\n"] + [f"\t{k[1]:5.2f}\t{k[2]:5.2f}\t{"YES" if k[0] else "NO "}\n" for k in [func(*[uniform(-2, 2) for j in range(2)]) for i in range(10)]]))

except ValueError:
    print("Ошибка")

