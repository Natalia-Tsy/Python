# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])
# print(*my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0
# for i in list_1:
#     if type(i) is int:
#         sum = sum + i
# print(sum)


# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# string_1 = ' '.join(map(str, list_1))
# print(string_1)
# for i in string_1.split():
#     if 'a' in i:
#         print(i)

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# line = (f'{list_1}')
# # print(line)
# for i in line.split():
#     if 'a' in i:
#         print(i)


# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# list2 = ['cat', 'dog', 'horse', 'cow']
# tuple2 = tuple(list2)
# print(tuple2)

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family_1 = input()
# family_2 = input()
# fam_list_1 = family_1.split(',')
# fam_list_2 = family_2.split(',')
# if len(fam_list_1) > len(fam_list_2):
#     print('Family 1 is larger')
# elif len(fam_list_2) > len(fam_list_1):
#     print('Family 2 is larger')
# else:
#     print('Families are equal') #почему выводит, если первая семья больше?

#3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
    # о вашем любимом фильме.
    # - распечатайте только ключи
    # - распечатайте только значения
    # - распечатайте пары ключ - значение
# my_dict = {
#     'title': 'Parasites',
#     'director': 'Pon dzhun-ho',
#     'year': 2019,
#     'budget': 1180000,
#     'main_actor': 'Son khan-ho',
#     'slogan':'Find the criminal'
# }
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dict = {'num1': 375,
#            'num2': 567,
#            'num3': -37,
#            'num4': 21
# }
# print(my_dict)
# for key in my_dict:
#     my_dict[key]
#     print(sum(my_dict.values()))
#     break

# print(sum(list(my_dict.values())))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list = [1, 2, 3, 4, 5, 3, 2, 1]
# print(list)
# new_set = set(list)
# print(new_set)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'},
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.difference(set2), set2.difference(set1))
# print(set1.issubset(set2))
# print(set1.issuperset(set2))
# print(set2.issubset(set1))
# print(set2.issuperset(set1))