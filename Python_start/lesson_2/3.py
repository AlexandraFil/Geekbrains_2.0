# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#Через dict (стоит ли так делать?)

my_dict = {1 : "Зима", 2 : "Зима", 3 : "Весна", 4 : "Весна", 5 : "Весна", 6 : "Лето", 7 : "Лето", 8 : "Лето", 9 : "Осень", 10 : "Осень", 11 : "Осень", 12 : "Зима"}

number_of_month = int(input('Введите номер месяца. '))

season = my_dict.get(number_of_month)

print(season)

# Через list (тот же вопрос)

my_list = ["Это зима!", 'Это весна!', 'Это осень!', "Это лето!"]

while True:
    number_of_month = int(input('Введите номер месяца. '))

    if number_of_month == 1 or number_of_month == 2 or number_of_month == 12:
         season = my_list[0]
         break
    elif 2 < number_of_month < 6:
        season = my_list[1]
        break
    elif 5 < number_of_month < 9:
        season = my_list[3]
        break
    elif 8 < number_of_month < 12:
        season = my_list[2]
        break
    else:
        print('Неправильно введен номер месяца! Введите число от 1 до 12!')
        continue

print(season)