'''4. Определить, какое число в массиве встречается чаще всего.'''

from random import randint

arr = []

for i in range(randint(1, 20)):
    arr.append(randint(0, 10))

print(f'Массив: {arr}')

num = arr[0]
max_count = 1

for i in range(len(arr) - 1):
    count = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count > max_count:
        max_count = count
        num = arr[i]

if max_count == 1:
    print("Все значения уникальны!")
else:
    print(f'Число {num} встречается наиболее часто - {max_count} раа.')