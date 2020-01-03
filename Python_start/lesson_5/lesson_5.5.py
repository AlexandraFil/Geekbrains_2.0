# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

sum_numbers = 0

with open('lesson_5.5.txt', 'w') as f:
    for i in range(20):
        number = randint(-99, 100)
        sum_numbers += number
        f.write(str(number) + " ")

print(f'Сумма чисел: {sum_numbers}')