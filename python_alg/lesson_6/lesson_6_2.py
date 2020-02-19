'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

import math
import sys

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

'''
Алгоритмы нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
'''


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

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {counting_function.__name__}: {size_of_all_variables} байт')

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

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {sieve_erato.__name__}: {size_of_all_variables} байт')

    return lst_prime[n-1]

'''
Общий размер используемых переменных в функции counting_function: 80 байт
Общий размер используемых переменных в функции sieve_erato: 26104 байт
Результат вызова функции sieve_erato(100): 541
'''

def sieve_erato_remove(n):

    lst_prime = [i for i in range(2, counting_function(n))]

    for number in lst_prime:
        if lst_prime.index(number) + 1 <= number:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {sieve_erato_remove.__name__}: {size_of_all_variables} байт')

    return lst_prime[n - 1]

'''
Общий размер используемых переменных в функции counting_function: 80 байт
Общий размер используемых переменных в функции sieve_erato_remove: 5236 байт
Результат вызова функции sieve_erato_remove(100): 541
'''

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

    local_variables_dict = locals().copy()
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Общий размер используемых переменных в функции {sieve_without_erato.__name__}: {size_of_all_variables} байт')

    return lst_prime[-1]

'''
Общий размер используемых переменных в функции sieve_without_erato: 3848 байт
Результат вызова функции sieve_without_erato(100): 541
'''

print(f'Результат вызова функции sieve_erato(100): {sieve_erato(100)}') #Для вычисления размера переменных необходимо выполнить функцию
print(f'Результат вызова функции sieve_erato_remove(100): {sieve_erato_remove(100)}')
print(f'Результат вызова функции sieve_without_erato(100): {sieve_without_erato(100)}')


'''
Первый вариант функции использует в разы больше места, чем другие два.
'''