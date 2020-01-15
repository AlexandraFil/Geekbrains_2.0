# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MyDate:
    def __init__(self, date_str):
        self.date_str = str(date_str)
        print(f"We have a new object now!")

    @classmethod
    def extraction(cls, date_str):
        date_list = date_str.split("-")

        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])

        new_list = [day, month, year]

        return new_list

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            pass
        else:
            return f'День {day} - проверьте правильно ли введен день.'
        if 1 <= month <= 12:
            pass
        else:
            return f'Месяц {month} - проверьте правильно ли введен месяц.'
        if 1 <= year <= 2020:
            return "Validation is completed: дата введена верно!"
        else:
            return f'Год {year} - проверьте правильно ли введен год.'

    def __str__(self):
        return f'Введена дата {MyDate.extraction(self.date_str)[0]}.{MyDate.extraction(self.date_str)[1]}.{MyDate.extraction(self.date_str)[2]}'

now = input('Введите число в формате дд-мм-гггг: ')
today = MyDate(now)
print(today)
print(f'Результат экстракции: {today.extraction(now)}')
print('Проверка чисел:')
print(today.validation(today.extraction(now)[0], today.extraction(now)[1], today.extraction(now)[2]))
