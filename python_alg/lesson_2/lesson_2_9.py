'''9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.'''

sum_max = 0
n_max = ""

while True:
    sum_curr = 0
    n = input('Введите число: ')
    for i in n:
        sum_curr += int(i)
    if sum_curr > sum_max:
        sum_max = sum_curr
        n_max = n

    more = input('Ввести еще число? Введите "Y" чтобы продолжить, введите "N" для завершения ввода чисел. ')
    if more != "y" and more != "Y":
        break

print(f'Наибольшая сумма цифр в числе {n_max}. Сумма цифр равна {sum_max}')
