# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):

    my_list = [arg1, arg2, arg3]
    result = sum(my_list) - min(my_list)
    return result

print(my_func(arg1 = int(input('Введите число: ')), arg2 = int(input('Введите число: ')), arg3 = int(input('Введите число: '))))