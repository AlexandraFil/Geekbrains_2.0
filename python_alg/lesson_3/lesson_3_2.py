'''2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.'''

from random import randint

arr = []

for i in range(randint(0, 20)):
    arr.append(randint(0, 20))

print(f'Массив: {arr}')

even = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even.append(i)

print(f'Индексы четных элементов: {even}')

