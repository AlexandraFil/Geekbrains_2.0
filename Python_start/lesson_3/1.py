# # 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# # Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(arg1, arg2):

    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        result = arg1 / arg2
    except ValueError:
        return "Программа работает только с числами!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return result

print(my_func(input("Введите число: "), input("Введите второе число: ")))
