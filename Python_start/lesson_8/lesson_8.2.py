# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionErr(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def division(x, y):
        try:
            result = x / y
            return result
        except:
            return f"Деление на ноль не предусмотренно!"


x = float(input("Введите делимое: "))
y = float(input("Введите делитель: "))

my_division = DivisionErr(x, y)
print(f'Результат деления: {my_division.division(x, y)}')
print(f'Результат деления: {DivisionErr.division(x, y)}')
