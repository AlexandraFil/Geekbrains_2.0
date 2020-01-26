'''9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''

import random

lines = int(input("Введите количество строк матрицы: "))
columns = int(input("Введите количество столбцов матрицы: "))

matrix = [[random.randint(1, 10) for _ in range(columns)] for _ in range(lines)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

# Для упрощения проверки работы программы - дает список минимальных значений в столбцах.

# min_list = []
#
# for j in range(columns):
#     min_c = matrix[0][j]
#     for i in range(1, lines):
#         if matrix[i][j] < min_c:
#             min_c = matrix[i][j]
#     min_list.append(min_c)
#
# print(min_list)

max_min = matrix[0][0]
for j in range(columns):
    min_c = matrix[0][j]
    for i in range(1, lines):
        if matrix[i][j] < min_c:
            min_c = matrix[i][j]
    if j == 0 or min_c > max_min:
        max_min = min_c

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min}.')
