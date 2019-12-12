income = int(input("Enter your income: "))
outgoing = int(input("Enter your expenses: "))

if income > outgoing:
    print("Поздравляем, Ваша фирма приносит прибыль!")
    profit = income - outgoing
    margin = profit / income

    print(f'Ваша прибыль: {profit}, ретнтабельность Вашей фирмы: {margin}.')

    count = int(input("Введите количество сотрудников: "))

    profit_for_1 = profit / count

    print(f"Прибыль в рассчете на одного сотрудника: {profit_for_1:.3f}.")

elif income == outgoing:
    print("Поздравляем, Ваша фирма не приносит убытка!")

else:
    print("Ваше предприятие убыточно!")