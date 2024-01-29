# some_list = []
# for i in range(5):
#     some_list.append(i)

# print(some_list)
# some_list = [i for i in range(5)]
# print(some_list)

# some_list = []
# for i in range(5):
#     if i % 2:
#         some_list.append(i**2)
# print(some_list)

# some_list = [i**2 for i in range(5) if i % 2]
# print(some_list)






# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())



# tuple
# value_list = [1, 23, 4]         # змінний
# value_tuple = (1, 23, 4)        # незмінний, займає менше памʼяті


# value_tuple = tuple()             # можна обозначити його так

# value_tuple = (1)               # Якщо один елемент БЕЗ КОМИ - не буде кортеж, буде стрінг або інта
# value_tuple = (1, )
#
#
# print(value_tuple, type(value_tuple))

# value_tuple = (1, 4, True, [1, 2, 3])         Можна редачити список в кортежі, бо список зберіг. як ЛІНКА
# value_tuple[-1].append('apple')
#
# print(value_tuple, type(value_tuple))

# value_tuple[0]
# value_tuple[0:]
# # value_tuple[::2]
# value_tuple = (1, 4, True, [1, 2, 3])
# value_list = list(value_tuple)
#
# print(value_list, type(value_list))

# value_tuple = (1, 4)
# value_1, *value_2 = value_tuple         # *value_2 - із залишених елементів створить список
#
# print(value_1)
# print(value_2)

# value_tuple = (1, 4)
# lenght, _ = value_tuple             # змінна _ означає як "непотрібна"
#
# print(lenght)
# print(_)
#
# for _ in range(5):
#     print('Hello')


####################### dict ######################


# value_dict = dict()
# value_dict = {}

# value_dict = dict(John=26, Andrew=28)
# value_dict = {"John": 26, "Andrew": 28}           Звичніше записувати ось так

# value_dict = {
#     "John": 26,
#     1: 28,
#     1.6: 25,                        # елементи перед : - це ключі
#     True: 22,
#     None: 28,
#     (1, 2, 3): 33,
# }
# print(value_dict)
# print(hash('John'))             # Хеш стрінги кожен раз змінюється
# print(hash(1))                  # Хеш int і bool - не змінюється
# print(hash(1.6))                # Хеш float зміниться при перезапуску компʼютера
# print(hash(True))
# print(hash([1, 2]))             # Хешувати не можна, бо список - змінний тип даних

# MD5, SHA256 - типи Хешування

# value_dict = {
#     "John": 26,
#     1: 28,
#     1.6: 25,                        # елементи перед : - це ключі
#     True: 22,
#     None: 28,
#     (1, 2, 3): [
#         {
#             "name": "John",
#             'age': 28,
#             'city': 'New York',  # елементи перед : - це ключі
#             'grade': 1,
#         },
#         {
#             'name': 'Nick',
#             'age': 20,
#             'city': 'New York',
#             'grade': 3,
#         }
#     ],
# }
#
# print(value_dict[None])         # Показує значення конкретного ключа
#
# value_dict[None] = 12           # змінює значення клуюча
#
# print(value_dict[None])
#
# value_dict['None'] = 12         # Створюється новий ключ в кінець дікта з значенням
#
# print(value_dict)

# person_1 = {
#             'name': 'Nick',
#             'age': 20,
#             'city': 'New York',
#             'grade': 3,
#         }
#
# person_2 = {
#             'name': 'John',
#             'age': 27,
#             'city': 'New York',
#             'grade': 1,
#         }
#
# group = [person_1, person_2]

# for i in person_1:
#     print(i, person_1[i])

# for key, value in person_1.items():           роздрукує ключі і значення
#     print(key, value)

# for key in person_1.keys():                   роздрукує ключі
#     print(key)

# for value in person_1.values():               роздрукує значення
#     print(value)



# this_dict = dict.fromkeys(('key1', 'key2', 'key3'))        # свторили пустий дікт, в який можемо щось всунути
# this_dict['key1'] = 'Nick'
# print(this_dict)
# print(thisdict)


# person_1 = {
#             'name': 'Nick',
#             'age': 20,
#             'city': 'New York',
#             'grade': 3,
#         }
#
# request = {}
# name = person_1.get('name', False)
# email = request.get('email', None)
# if not email:
#     print('error')
# print(name)



##### pop #####

# print(person_1)
# value = person_1.pop('name')
# print(value)
# print(person_1)


##### update() ####

# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
#
# print(car)
# car['color'] = 'White'
# car.update({'color': 'White'})        два способи додати в дікт


# some_list = [i**2 for i in range(5)]
# print(some_list)

# dict comprehension

# value_dict = {i: f"This is {i}" for i in range(1, 7)}
#
# print(value_dict)
#
# value_dict = {
#     1: 'This is 1',
#     2: 'This is 2',
#     3: 'This is 3',
#     4: 'This is 4',
#     5: 'This is 5',
#     6: 'This is 6'
# }





############# SET #############

# value_set = set()
# value_list = [1, 'apple', 3, 'bug', 5, 1, 1, 1, 2, 3,]
# # print(value_list)
# # print(set(value_list))              # Прибирає повт. числа і зберігає особливі по порядку. Стрінга "пригає"
#
# # value_str = 'apple'
# # print(value_str)
# # print(set(value_str))
#
# value_set = set(value_list)
# new_value_list = list(value_set)
# print(value_list, type(value_list))
# print(value_set, type(value_set))
# print(new_value_list, type(new_value_list))

# value_set_1 = {1, 2, 3}
# value_set_2 = {7, 6, 5, 1}
# print(value_set_1.union(value_set_2))   # Обʼєднує
#
# # difference()
#
# print(value_set_1.difference((value_set_2)))    # Виділяє те, чого немає в другому сеті
#
# # intersection()
# print(value_set_1.intersection(value_set_2)) # Виділяє спільне в двух сетах












