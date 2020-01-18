'''3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.'''

from random import randint, uniform, randrange

type_range = input('Введите тип (int - целые числа, float - вещественные числа, str - буквы): ')
start = input('Введите начало диапазона: ')
end = input('Введите конец диапазона: ')

if type_range == 'int':
    if int(start) <= int(end):
        result = randint(int(start), int(end))
    else:
        result = randint(int(end), int(start))

elif type_range == 'float':
    if float(start) <= float(end):
        result = uniform(float(start), float(end))
    else:
        result = uniform(float(end), float(start))

else:
    if ord(start) <= ord(end):
        result = chr(randrange(ord(start), ord(end) + 1))
    else:
        result = chr(randrange(ord(end), ord(start) + 1))

print(f'Ваш случайный элемент: {result}.')

