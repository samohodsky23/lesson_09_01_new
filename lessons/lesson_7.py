# Lesson 7

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

# my_set = {1, 2, 3, 'hello', 'red'}
# my_list = [2, 3, 'hello', 'red', 1, ]
#
# print(1 in my_set, type(my_set))
# print(1 in my_list)
#
# new_val = frozenset(my_set)
# print(new_val)

# (1, 2, 3): 'rgb'

# ('www.site.com', 'www.site_2.com')


from collections import OrderedDict, defaultdict


# value_dict = {'name': 'Nick',
#               'age': 18,
#               'country': 'Ukraine'
# }
# print(value_dict)

# my_order_dict = OrderedDict(value_dict)     # OrderedDict([('name', 'Nick'), ('age', 18), ('country', 'Ukraine')])
# питають на співбесідах
# print(my_order_dict)
#
# this_dict = dict.fromkeys(('name', 'age', 'country'), [])
#
# print(this_dict)
# this_dict['name'].append(2)
#
# print(this_dict)

# my_dict = defaultdict()


# from collections import namedtuple
#
# fields = ('color', 'engine')
#
# car = namedtuple('Auto', fields)
#
# car_1 = car('red', 200)
#
# print(car_1)
#
# color_1, engine_1 = car_1
# # print(color_1, engine_1)
# #
# # print(car_1.color)
# # print(car_1.engine)
# print(car_1._asdict())


########## Functions ########### def

#
# def math_add(num_1, num_2):
#     adding = num_1 + num_2
#
#     return adding
#
#
# def calc(num_1, num_2, operator):
#     if operator == '+':
#         result = math_add(num_1, num_2)
#         return result
#
#
# def my_func():
#     pass
#
#
# print(calc(1, 3, '+'))




# def say_hi(name, age):
#     pass
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')