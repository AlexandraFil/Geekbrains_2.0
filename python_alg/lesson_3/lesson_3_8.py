'''8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу.'''

size = 4
matrix = [[0 for _ in range(size + 1)] for i in range(size)]

for i in range(size):
    print(f'Строка {i + 1}:')
    for j in range(size):
        matrix[i][j] = int(input(f'Введите число {j + 1} столбец: '))
        matrix[i][size] += matrix[i][j]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
