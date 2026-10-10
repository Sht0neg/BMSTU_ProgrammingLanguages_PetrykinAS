from random import uniform


def print_array(arr: list):
    for i in arr:
        print(f"{i: 7.3f}", end=" ")


n = int(input("Задайте количество элементов в массиве (N<=30) N: "))

arr = [uniform(-5, 5) for i in range(n if n < 30 else 30)]

count_of_negatives = sum(map(lambda x: 1 if x < 0 else 0, arr))

min_abs = min(arr, key=lambda x: abs(x))
sum_after_min_abs = sum(map(abs, arr[arr.index(min_abs if min_abs in arr else -min_abs) + 1:]))

sorted_arr = sorted(map(lambda x: x ** 2 if x < 0 else x, arr))


print("Начальное состояние:")
print_array(arr)
print(f"\nКолличество отрицательных элементов массива: {count_of_negatives}")
print(f"Минимальный по модулю элемент массива: {min_abs: 7.3f}, сумма элементов после минимального: {sum_after_min_abs: 7.3f}")
print("Отсортированный массив, в котором отрицательные числа возведены в квадрат:")
print_array(sorted_arr)
