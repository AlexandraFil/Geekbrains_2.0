'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''

from random import randint

arr = []

for i in range(randint(1, 20)):
    arr.append(randint(0, 20))

print(f'Массив: {arr}')

min_i = 0
max_i = 0

for i in range(1, len(arr)):
    if arr[i] < arr[min_i]:
        min_i = i
    elif arr[i] > arr[max_i]:
        max_i = i
print(f'Минимальный элемент: {arr[min_i]}')
print(f'Максимальный элемент: {arr[max_i]}')

sum_el = 0

if min_i == max_i:
    pass
elif min_i < max_i:
    for i in range(min_i + 1, max_i):
        sum_el += arr[i]
else:
    for i in range(max_i + 1, min_i):
        sum_el += arr[i]

print(f'Сумма элементов между ними: {sum_el}')