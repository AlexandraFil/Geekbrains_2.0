'''2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''

n = input('Введите натуральное число: ')
even = 0
odd = 0

for i in n:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'В числе {n} {even} четные и {odd} нечетные цифры.')
