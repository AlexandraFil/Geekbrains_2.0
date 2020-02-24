'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''
from random import randint
size = 10
array = [randint(0, 50) for _ in range(size)]


def merge_sort(array):
    if len(array) > 1:
        center = len(array) // 2
        left = array[:center]
        right = array[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        return array


print('Исходный массив:', array)
print('Сортировка слиянием:', merge_sort(array[:]))
