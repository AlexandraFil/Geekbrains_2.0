'''1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из
модуля collections
'''


import collections

count_companies = int(input('Введите количество компаний: '))

companies = []

for i in range(count_companies):
    title = input('Введите название компании: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Ввведите квартальные прибыли через пробел: ').split(' '))
    company = {
        'title': title,
        'profit_q1': profit_q1,
        'profit_q2': profit_q2,
        'profit_q3': profit_q3,
        'profit_q4': profit_q4,
        'profit_year': profit_q1 + profit_q2 + profit_q3 + profit_q4,
    }

    companies.append(company)

profit_col = collections.Counter()

for company in companies:
    profit_comp = company.copy()
    del profit_comp['title']
    profit_col += collections.Counter(profit_comp)

print()
for company in companies:
    print(company)

average_profit = profit_col['profit_year'] / len(companies)

print(f'Суммарная прибыль: {profit_col}')
print(f'Средняя годовая прибыль компаний: {average_profit}')
print('Компании, где прибыль выше среднего: ', [x['title'] for x in companies if x['profit_year'] >= average_profit])
print('Компании, где прибыль ниже среднего: ', [x['title'] for x in companies if x['profit_year'] < average_profit])