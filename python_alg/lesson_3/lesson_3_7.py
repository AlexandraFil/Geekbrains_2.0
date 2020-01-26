'''7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.'''

from random import randint

arr = []

for i in range(randint(2, 20)):
    arr.append(randint(-20, 20))

print(f'Массив: {arr}')

if arr[0] < arr[1]:
    min1, min2 = 0, 1
else:
    min1, min2 = 1, 0

for i in range(2, len(arr)):
    if arr[i] <= arr[min1]:
        min2 = min1
        min1 = i
    elif arr[i] < arr[min2]:
        min2 = i

print(f'Два наименьших элемента: {arr[min1]} (индекс {min1}), {arr[min2]} (индекс {min2}).')



