# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.lists]))

    # def __str__(self):
    #     return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        result = []
        num = []
        if len(self.lists) == len(other.lists):
            for i in range (len(self.lists)):
                for j in range (len(self.lists[i])):
                    num.append(self.lists[i][j] + other.lists[i][j])
                    if len(num) == len(self.lists[i]):
                        result.append(num)
                        num = []

        else:
            print("Сложение матриц невозможно!")
        return result

matrix_1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
matrix_2 = Matrix([[3, 2, 1], [5, 4, 3], [7, 6, 5]])

print(f'Первая матрица:\n{matrix_1}')
print(f'Вторая матрица:\n{matrix_2}')

matrix_sum = Matrix(matrix_1 + matrix_2)

print(f'Сумма:\n{matrix_sum}')
