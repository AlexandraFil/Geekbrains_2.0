'''4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.'''

character_1 = input('Введите букву: ')
character_2 = input('Введите вторую букву: ')

ord_1 = ord(character_1.lower()) - 96
ord_2 = ord(character_2.lower()) - 96

if ord_1 != ord_2:
    between = abs(ord_1 - ord_2) - 1
else:
    between = 0

print(f'Буква {character_1} стоит на {ord_1} месте, буква {character_2} стоит на {ord_2} месте.\nМежду ними находится {between} букв.')