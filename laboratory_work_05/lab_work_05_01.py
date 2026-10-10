from random import randint

n, m = map(int, input("Введите размер матрицы (NxM): ").split("x"))

def fill_matrix(n: int, m: int = 0) -> list:
    matrix = [[randint(-10, 10) for j in range(m)] for i in range(n)]
    return matrix

def sorted_matrix_by_count_of_reapeted_elements(matrix: list) -> float:
    return sorted(matrix, key=lambda x: len(x) - len(set(x)))

def first_positive_string_of_matrix(matrix: list, n: int, m: int) -> int:
    temp_list = [i for i in range(m)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < 0 and j in temp_list:
                temp_list.remove(j)
    return temp_list[0] if len(temp_list) > 0 else "В каждом столбце есть хотя бы один отрицательный элемент"

def print_matrix(matrix: list) -> None:
    for i in matrix:
        for j in i:
            print(f"{j:3}", end="  ")
        print("\n")

matrix = fill_matrix(n, m)
print_matrix(matrix)
print("Матрица отсортированная по строкам с возрастающим кол-вом повторяющихся элементов\n")
print_matrix(sorted_matrix_by_count_of_reapeted_elements(matrix))
print(f"Первый столбец со всеми не отрицательными элементами: {first_positive_string_of_matrix(matrix, n, m)}")
