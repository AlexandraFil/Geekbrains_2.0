'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
'''

from random import randint
size = 9
array = [randint(0, 50) for _ in range(size)]
print(array)

def cocktail_sort(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
        left += 1

cocktail_sort(array)
print(array)

def median(array): # работает с отсортированным массивом
    half = len(array) // 2
    if not len(array) % 2:
        return (array[half - 1] + array[half]) / 2
    return array[half]

print('Медиана:', median(array))