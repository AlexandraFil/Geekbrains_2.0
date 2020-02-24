'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''

from random import randint
from timeit import timeit

size = 10
executions = 10000

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array

def bubble_sort_smart(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break


    return array

array = [randint(-100, 100) for _ in range(size)]
print(array)
print(bubble_sort_smart(array))

time1 = timeit(f'bubble_sort_smart({array})',
              setup='from __main__ import bubble_sort_smart',
              number=executions)
time2 = timeit(f'bubble_sort({array})',
              setup='from __main__ import bubble_sort',
              number=executions)
print(time1)
print(time2)