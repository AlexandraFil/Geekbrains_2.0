# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

wages = {}
with open('lesson_5.3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        wages[line.split()[0]] = float(line.split()[1])
print('Сотрудники, получающие меньше 20 000: ', end= " ")
for surname, salary in wages.items():
    if salary < 20000:
        print(surname, end= ", ")
print(f"cредняя величина дохода сотрудников: {sum(wages.values())/len(wages)}")