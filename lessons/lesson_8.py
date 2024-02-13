# Lesson 8. Функції, частина 2.

# Перепиши 6-ту домашку функцією!!


##### Definitions pt. 2 ######

# def my_func(num_1, num_2):
#     res = 0
#     if num_2 == 0:
#         res = "Error"
#     else:
#         res = num_1 + num_2
#         return res
#
#     print('!!!!!!!')
#
# print(my_func(2, 3))


# def my_add(num_1, num_2):       # Приклад локальних змінних
#
#     result = num_1 + num_2
#
#     print(locals())
#
#     return result
#
# result = 10
#
# print(my_add(3, 2))
# print(result)

####### LEGB ########### Правила доступу до змінних

# Enclosing




# from math import pi

# pi = 'global'

# def outer():
#     # pi = 'Enclosing'
#
#     def inner():
#         # pi = 'Local'
#         print(pi)
#
#     inner()
#
# outer()
# print(pi)
# Викликає local -> enclosing -> global -> built in

# def outer():
#     pi = 'Enclosing'
#
#     def inner():
#         # pi = 'Local'
#         pi += '!!!!'        # Видасть помилку, якщо порушує логіку коду
#         print(pi)
#
#     inner()
#
# outer()
# print(pi)





# import operator
#
# actions = {
#     '+': operator.add,            Ці фукціїї завжди приймають по 2 елементи ( робота під капотом )
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,
# }
# num_1 = float(input('num_1 '))            # Калькулятор через функцію
# action = input('action ')
# num_2 = float(input('num_2 '))
#
# func = actions.get(action)
# if not func:
#     print('Error')
# else:
#     print(func(num_1, num_2))

# is_send_second_email = True

# def print_line(w, fill, is_email=False):
#     for i in range(w):
#         print(fill, end="")
#     if is_email:
#         print('yes')
#
#     return
#
# # print_line(6, '*')
# # print_line(fill="*", w=6, is_email=is_send_second_email)       # іменований виклик
# print_line(6, "*", is_email=True)

# *args ############

# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# val_1, *tmp = my_tuple
# print(val_1)
# print(tmp)


# def my_func(val_1, *args):
#
#     return val_1
#
# print(my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def group(teacher, *args):
#     print(args)
#     res = {'teacher': teacher, 'students_list': list(args)}
#     # for student in args:
#     #     res['students_list'].append(student)
#     return res
#
#
# print(group("Nick", 'Volodymyr', 'Stepan'))



# def get_min_val(*args):
#     print('!!!!!!!!!!')
#     # min_val = args[0]
#     min_val = None
#     if not args:
#         return 'Error'
#     else:
#         min_val = args[0]
#         for i in args:
#             if i < min_val:
#                 min_val = i
#     return min_val
#
# print(get_min_val(1, 2, 3))


# **kwargs          dict{}

# def say_hello(name):
#     return f'Hello {name}'
# def print_age(age):
#     return f'{age}'
# def print_line(w, fill, **kwargs):
#     print(kwargs)
#     if 'name' in kwargs:
#         print(say_hello(kwargs.pop('name')))
#     else:
#         print(say_hello('John'))
#
#     print(print_age(kwargs.pop('age')))
#
#     for i in range(w):
#         print(fill, end='')
#
#     return
#
# print_line(6, '*', name_2='Nick', age=18)






