'''7. Определить, является ли год, который ввел пользователь, високосным или не високосным.'''

year = int(input('Введите год: '))

if year % 4 != 0:
    print(f"Год {year} невисокосный.")
elif year % 100 != 0:
    print(f"Год {year} високосный.")
elif year % 400 != 0:
    print(f"Год {year} невисокосный.")
else:
    print(f"Год {year} високосный.")