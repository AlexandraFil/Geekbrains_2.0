'''5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.'''

from random import randint

arr = []

for i in range(randint(0, 20)):
    arr.append(randint(-20, 20))

print(f'Массив: {arr}')

index = -1

for i in range(len(arr)):
    if arr[i] < 0:
        if index == -1 or arr[i] > arr[index]:
            index = i

if index == -1:
    print('В массиве нет отрицательных чисел!')
else:
    print(f'Максимальное отрицательное число в массиве {arr[index]} имеет индекс {index}.')
