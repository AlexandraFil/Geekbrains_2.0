'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

from random import randint

arr = []

for i in range(randint(1, 20)):
    arr.append(randint(0, 20))

print(f'Массив первоначальный: {arr}')

min_i = 0
max_i = 0

for i in range(1, len(arr)):
    if arr[i] < arr[min_i]:
        min_i = i
    elif arr[i] > arr[max_i]:
        max_i = i

print(f'Минимальный элемент: {arr[min_i]}')
print(f'Максимальный элемент: {arr[max_i]}')

spam = arr[min_i]
arr[min_i] = arr[max_i]
arr[max_i] = spam

print(f'Итоговый массив: {arr}')