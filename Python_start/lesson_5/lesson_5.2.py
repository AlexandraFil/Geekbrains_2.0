# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("lesson_5.2.txt") as f:
    line = f.readlines()
    for index, value in enumerate(line, 1):
        words_in_line = len(value.split())
        print(f"Строка {index} содержит {words_in_line} слов.")