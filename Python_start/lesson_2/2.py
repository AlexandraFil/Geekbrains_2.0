# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

while True:
    my_list.append(input('Введите значение: '))
    answer = input('Продолжить вводить значения? (Введите "yes" чтобы продолжить) ')
    if answer == "yes":
        my_list.insert(len(my_list)-1, input('Введите значение: '))
        answer = input('Продолжить вводить значения? (Введите "yes" чтобы продолжить) ')
        if answer == "yes":
            continue
        else:
            break
    else:
        break

print(my_list)

"""
a = input('Введите элементы для массива разделяя их пробелами: ').split()
i = 0
print(f'Оригинальный список {a}')
while i + 1 < len(a):
if i % 2 == 0:
a.insert(i, a.pop(i + 1))
i += 1
print(f'Измененный список {a}')
"""
