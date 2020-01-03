# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    line = input("Введите строку: ").split()
    if len(line) == 0:
        break
    with open("new_1.txt", "a") as f:
        for i in range(len(line)):
            print(line[i], file=f)


