# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name = "ivan", surname = "smith", year_of_birth = "2000", city = "Moscow", email = "Не указан", phone_number = "Не указан"):
    if name == "":
        name = 'Аноним'
    if surname == '':
        surname = "Анонимович"
    if year_of_birth == "":
        year_of_birth = "0000"
    if city == "":
        city = "N"
    return f'Вас зовут {name} {surname}. Вы родились в {year_of_birth} году и проживаете сейчас в городе {city}.  Мы можем написать вам на Вашу почту: {email}, или же звонить сюда {phone_number}.'

print(my_func(name = input('Введите свое имя: '), surname = input('Введите свою фамилию: '), year_of_birth = input('Год рождения: '), city = input('В каком городе проживаете? '), email = input('Ваша электронная почта: '), phone_number = input('Укажите номер телефона для связи: ')))