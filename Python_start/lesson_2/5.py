# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

# my_list = [7, 5, 3, 3, 2]
#
# new_number = int(input('Введите число: '))
#
# if new_number > my_list[0]:
#     my_list.insert(0, new_number)
# elif new_number <= my_list[-1]:
#     my_list.append(new_number)
# else:
#     if new_number in my_list:
#         ind = my_list.index(new_number)
#         count = my_list.count(new_number)
#         my_list.insert((ind + count), new_number)
#     else:
#         i=1
#         if my_list[i] > new_number:
#             my_list.insert(i+1, new_number)
#         else:
#             i += 1
#
# print(my_list)







