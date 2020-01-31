'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

# a. выбрать хорошую задачу, которую имеет смысл оценивать,
'''Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…'''

# b. написать 3 варианта кода (один у вас уже есть),

import cProfile

# Вариант 1

def sum_1(n):
    sum_num = 0
    i = 1
    for num in range(n):
        sum_num += i
        i /= -2
    return sum_num

# Вариант 2
'''Последовательность разбивается на две подпоследовательности,
    каждая из которых является геометрической последовательностью. Нужно рассмотреть два случая:
    когда  n четное, а когда нечетное, для каждого из случаев вывести формулу.'''

def get_sum_though_equation(i: int, j: int) -> float:
    return ((0.25 ** i) - (0.25 ** j / 2) - 0.5) / -0.75

def sum_2(n):
    if n % 2 != 0:
        series_sum = get_sum_though_equation(i=n // 2 + 1, j=n // 2)
    else:
        series_sum = get_sum_though_equation(i=n // 2, j=n // 2)

    return series_sum

# Вариант 3

def sum_3(n):
    cycle_sum = 0
    for i in range(0, n):
        cycle_sum += ((-1) ** i) / (2 ** i)
    return cycle_sum

# c. проанализировать 3 варианта и выбрать оптимальный,

# "lesson_4_1.sum_1(10)"
# 100 loops, best of 5: 1.24 usec per loop

# "lesson_4_1.sum_1(100)"
# 100 loops, best of 5: 7.54 usec per loop

# "lesson_4_1.sum_1(1000)"
# # 100 loops, best of 5: 86.6 usec per loop

# "lesson_4_1.sum_2(10)"
# 100 loops, best of 5: 558 nsec per loop

# "lesson_4_1.sum_2(100)"
# 100 loops, best of 5: 569 nsec per loop

# "lesson_4_1.sum_2(1000)"
# 100 loops, best of 5: 582 nsec per loop

# "lesson_4_1.sum_3(10)"
# 100 loops, best of 5: 5.94 usec per loop

# "lesson_4_1.sum_3(100)"
# 100 loops, best of 5: 82.6 usec per loop

# "lesson_4_1.sum_3(1000)"
# 100 loops, best of 5: 1.51 msec per loop

# Как видно из результатов замеров, второй вариант в разы быстее других двух, потому его будем считать оптимальным.
# Из двух других вариантов решения первый быстрее и проще в понимании, потому его ставим на второе место.
# Как видно далее из отчетов cProfile третий способ значительно медленнее при работе с большими цифрами.

# cProfile.run('sum_1(100000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#         1    0.018    0.018    0.018    0.018 lesson_4_1.py:20(sum_1)
#         1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sum_2(100000)')
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_1.py:33(get_sum_though_equation)
#         1    0.000    0.000    0.000    0.000 lesson_4_1.py:36(sum_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sum_3(100000)')
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   15.344   15.344 <string>:1(<module>)
#         1   15.344   15.344   15.344   15.344 lesson_4_1.py:46(sum_3)
#         1    0.000    0.000   15.344   15.344 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



