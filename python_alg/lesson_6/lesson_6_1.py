'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

import sys

# print(sys.version, sys.platform)

# 3.7.5 (default, Oct 25 2019, 10:52:18) [Clang 4.0.1 (tags/RELEASE_401/final)] darwin

def show_size(x, level=0):
    result_size = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size

# Вариант 1

def sum_1(n):
    sum_num = 0
    i = 1
    for num in range(n):
        sum_num += i
        i /= -2

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {sum_1.__name__}: {size_of_all_variables} байт')

    return sum_num

print(f'Результат вызова функции: {sum_1(100)}') #Для вычисления размера переменных необходимо выполнить функцию


'''
Список всех переменных: {'n': 10, 'sum_num': 0.666015625, 'i': 0.0009765625, 'num': 9}
 type=<class 'int'>, size=28, obj=10
 type=<class 'float'>, size=24, obj=0.666015625
 type=<class 'float'>, size=24, obj=0.0009765625
 type=<class 'int'>, size=28, obj=9
Общий размер используемых переменных в функции sum_1: 104 байт
Результат вызова функции: 0.666015625
'''


# Вариант 2
'''Последовательность разбивается на две подпоследовательности,
    каждая из которых является геометрической последовательностью. Нужно рассмотреть два случая:
    когда  n четное, а когда нечетное, для каждого из случаев вывести формулу.'''

def get_sum_though_equation(i: int, j: int) -> float:

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {get_sum_though_equation.__name__}: {size_of_all_variables} байт')
    return ((0.25 ** i) - (0.25 ** j / 2) - 0.5) / -0.75

'''
Список всех переменных: {'i': 5, 'j': 5}
 type=<class 'int'>, size=28, obj=5
 type=<class 'int'>, size=28, obj=5
Общий размер используемых переменных в функции get_sum_though_equation: 56 байт
'''

def sum_2(n):
    if n % 2 != 0:
        series_sum = get_sum_though_equation(i=n // 2 + 1, j=n // 2)
    else:
        series_sum = get_sum_though_equation(i=n // 2, j=n // 2)

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {sum_2.__name__}: {size_of_all_variables} байт')

    return series_sum

print(f'Результат вызова функции: {sum_2(100)}')


'''
Список всех переменных: {'n': 10, 'series_sum': 0.666015625}
 type=<class 'int'>, size=28, obj=10
 type=<class 'float'>, size=24, obj=0.666015625
Общий размер используемых переменных в функции sum_2: 52 байт
Результат вызова функции: 0.666015625
'''

# Вариант 3

def sum_3(n):
    cycle_sum = 0
    for i in range(0, n):
        cycle_sum += ((-1) ** i) / (2 ** i)

    local_variables_dict = locals().copy()  # Копируем на всякий случай
    # Так как последующие переменные были заданы после вызова функции copy, то можно сказать, что это будет размер,
    # занимаемый переменными в чистом виде.
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {sum_3.__name__}: {size_of_all_variables} байт')

    return cycle_sum

print(f'Результат вызова функции: {sum_3(100)}')

'''
Список всех переменных: {'n': 10, 'cycle_sum': 0.666015625, 'i': 9}
 type=<class 'int'>, size=28, obj=10
 type=<class 'float'>, size=24, obj=0.666015625
 type=<class 'int'>, size=28, obj=9
Общий размер используемых переменных в функции sum_3: 80 байт
Результат вызова функции: 0.666015625
'''

'''Наименьшее количество памяти в данном случае для sum_3'''