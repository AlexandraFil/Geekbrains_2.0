# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 1.1, 34.56, False, (1, 2, 3, 4), True, ['one', "two"], 'Str', {1, 1, 3, 5}, {1 : 1, 2 : 2}]

for i in my_list:
    print(type(i))
