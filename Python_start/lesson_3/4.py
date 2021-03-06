# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора *. Второй — более сложная реализация без оператора *, предусматривающая использование цикла.

def my_func(x, y):

    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return "Программа работает только с числами!"

    if x < 0 or y > 0 or (y % 1) != 0 :

        return "По условиям задачи 'Программа принимает действительное положительное число x и целое отрицательное число y', Ваши значения не подходят!"

    else:

        # result = x**y
        # return result
        #
        # result = pow(x, y)
        # return result

        result = 1
        for i in range(abs(y)):
            result *= x
        return 1 / result

print(my_func(input("Введите x: "), input("Введите y: ")))
