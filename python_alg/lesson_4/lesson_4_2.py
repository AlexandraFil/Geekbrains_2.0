'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
'''

'''
Написано три функции, в результате самая первая с использованием решета Эратосфена самая быстрая. 
'''

import cProfile
import math

'''
Функция возвращает верхнюю границу отрезка на котором лежат i-e количество простых чисел. 
Функция основана на теореме о распределении простых чисел. 
Количество простых чисел на отрезке [1;n] растёт с увеличением n как n / ln(n).
'''

def counting_function(n):
    '''
    Функция возвращает верхнюю границу отрезка на котором лежат i-e количество простых чисел.
    Функция основана на теореме о распределении простых чисел.
    Количество простых чисел на отрезке [1;n] растёт с увеличением n как n / ln(n).
    '''

    number_of_primes = 0
    number = 2
    while number_of_primes <= n:
        number_of_primes = number / math.log(number)
        number += 1
    return number

def sieve_erato(n):

    n_max = counting_function(n)

    sieve = [i for i in range(n_max + 1)]
    sieve[1] = 0
    for i in range(2, n_max):
        if sieve[i] != 0:
            j = i * 2
            while j < n_max:
                sieve[j] = 0
                j += i
    lst_prime = [i for i in sieve if i != 0]
    return lst_prime[n-1]

# "lesson_4_2.sieve_erato(10)"
# 100 loops, best of 5: 19.5 usec per loop
# "lesson_4_2.sieve_erato(100)"
# 100 loops, best of 5: 402 usec per loop
# "lesson_4_2.sieve_erato(200)"
# 100 loops, best of 5: 939 usec per loop
# "lesson_4_2.sieve_erato(1000)"
# 100 loops, best of 5: 6.26 msec per loop

def sieve_erato_remove(n):

    lst_prime = [i for i in range(2, counting_function(n))]

    for number in lst_prime:
        if lst_prime.index(number) + 1 <= number:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[n - 1]

# "lesson_4_2.sieve_erato_remove(10)"
# 100 loops, best of 5: 52.2 usec per loop
# "lesson_4_2.sieve_erato_remove(100)"
# 100 loops, best of 5: 11 msec per loop
# "lesson_4_2.sieve_erato_remove(200)"
# 100 loops, best of 5: 57.3 msec per loop

def sieve_without_erato(n):

    lst_prime = [2]
    number = 3
    while len(lst_prime) < n:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

#"lesson_4_2.sieve_without_erato(10)"
# 100 loops, best of 5: 12.6 usec per loop
# "lesson_4_2.sieve_without_erato(100)"
# 100 loops, best of 5: 578 usec per loop
# "lesson_4_2.sieve_without_erato(200)"
# 100 loops, best of 5: 1.94 msec per loop
# "lesson_4_2.sieve_without_erato(1000)"
# 100 loops, best of 5: 45.6 msec per loop


# cProfile.run('sieve_erato(1000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.007    0.007    0.010    0.010 lesson_4_2.py:21(counting_function)
#         1    0.003    0.003    0.015    0.015 lesson_4_2.py:35(sieve_erato)
#         1    0.001    0.001    0.001    0.001 lesson_4_2.py:39(<listcomp>)
#         1    0.000    0.000    0.000    0.000 lesson_4_2.py:47(<listcomp>)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#      9118    0.003    0.000    0.003    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sieve_erato_remove(1000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.000    4.000 <string>:1(<module>)
#         1    0.003    0.003    0.005    0.005 lesson_4_2.py:21(counting_function)
#         1    3.782    3.782    4.000    4.000 lesson_4_2.py:50(sieve_erato_remove)
#         1    0.002    0.002    0.002    0.002 lesson_4_2.py:52(<listcomp>)
#         1    0.000    0.000    4.000    4.000 {built-in method builtins.exec}
#      1130    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      9118    0.002    0.000    0.002    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1130    0.010    0.000    0.010    0.000 {method 'index' of 'list' objects}
#      7988    0.201    0.000    0.201    0.000 {method 'remove' of 'list' objects}

# cProfile.run('sieve_without_erato(1000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.083    0.083 <string>:1(<module>)
#         1    0.070    0.070    0.083    0.083 lesson_4_2.py:64(sieve_without_erato)
#         1    0.000    0.000    0.083    0.083 {built-in method builtins.exec}
#      7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#       999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      7917    0.011    0.000    0.011    0.000 {method 'copy' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


