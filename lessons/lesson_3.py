# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# list
# змінні, не змінні типи даних різниця
# методи list(append(), pop(), sort(), copy())
# функція sorted()

########## NoneType ###########

# value = None
# val_1 = id(value)
# print(val_1)      Виведе номер ячейки

# value = 11111
# val_1 = print(value)    Виведе текст value і None
# print(val_1)

# value = None
# print(value)       None
# value = 111        Приклад динамічної типізації. Може гнучко змінювати свій тип даних
# print(value)       111

############# Bool #################

# value_int = 1
# print(bool(value_int))       True
# value_int = 0
# print(bool(value_int))       False
# value_int = -1                Все, що не 0 - True
# print(bool(value_int))       True

# value_float = 0.001
# print(bool(value_float))       True, бо вже не повністю 0

# value_str = " "
# print(bool(value_str))        True
# value_str = ""                False
# print(bool(value_str))

# value_bool = True
# print(value_bool * 2)         Output: 2 | Приклад Duck typing, іноді питають на співбесідах

# value_int = 100
# print(bool(value_int) * 2)   Output: 2


################## Logic operators ################     >, <, >=, <=, ==, !=, is, not, in

# value_1 = 1
# value_2 = 5
# print(value_1 > value_2)      Output: False

# print("he" in "hello")        Output: True | частинка "he" є в строкі "hello"
# print("He" in "hello")        Output: False | частинки "He" немає в строкі "hello"

# print("hello" != "hello")     Output: False

# value_1 = 'hello'
# value_2 = 'hello'
# print('hello' == 'hello')     Output: true |
# print(value_1 is value_2)     Output: true |

## if певна дія:
#     виконуємо цю операцію


# value_int = 1
#
# if value_int > 0:
#     print(f"{value_int} is bigger than 0")
#
# print('end')

# value_int = 11
#
# if value_int > 10:
#     print(f'{value_int} is bigger than 0')
# elif value_int > 0:
#     print(f'{value_int} is bigger than 10')
# else:
#     print(f'{value_int} is not bigger than 0')        Будь уважним, і будуй конструкцію правильно
#
# print('end')

# value_int = 11

# if value_int > 0 and value_int < 10:
# if 0 < value_int < 10:                        | Спростував код, так РЕР8 не лається
#     print(f'{value_int} is bigger than 0')
# elif value_int > 10:
#     print(f'{value_int} is bigger than 10')
# else:
#     print(f'{value_int} is not bigger than 0')


######### Programming golf ###########
# Забава у програмістів, спроба написати якийсь код якумого комплектним ( в ідеалі в 1 строчку)
# Дозволяє розуміти мову краще

# Example:
# Short Hand If:
# if a > b: print('a is greater than b')
# Short Hand If...Else
#
# value_1 = 2
# value_2 = 330
#
# # if value_1 > value_2:
# #     result = 'A'
# # else:
# #     result = 'B'
#
#
# result = "A" if value_1 > value_2  else 'B'    | Тернарний оператор (!) | Буде плюсом на співбесіді
#
# print(result)



############# List ################ часто перевіряють, треба знати ідеально

# value_list = [1, 2.1, 'hello', [1, 2, 3]] # Можемо покласти сюди все | 0, 1, 2, 3

# print(value_list)
# print(value_list[0])
# print(value_list[-1])
# print(value_list[-2])

# print(len(value_list)) # lenght
# print(value_list[0:2]) # 0 - входить в діапазон | 2 - до(не входить в діапазон)

# print(value_list[0:])   # Output: [1, 2.1, 'hello', [1, 2, 3]]
# print(value_list[4:])   # Output: []
# print(value_list[10:])   # Output: [] | Як недобудований дім, можуть добудувати список
# print(value_list[-10:])   # Output: []

# print(value_list[1:])   # немає помилки навіть якщо не існує індекса
# print(value_list[-2:10])    #

##########################################
#
# base_list = [1, 2, 3]
# my_new_list = base_list * 4
#
# print(my_new_list)


# base_list = [1, 2, 3]
# new_list = [base_list] * 4
#
# print(new_list)       [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
#
# base_list[0] = 10
#
# print(new_list)      [[10, 2, 3], [10, 2, 3], [10, 2, 3], [10, 2, 3]]

# base_list = [1, 2, 3]
#
# new_list = [base_list.copy()] * 4
#
# base_list[0] = 10
# print(f'base_list {base_list}')
# print(new_list)

# base_list = [1, 2, 3, [True, False]]
#
# new_list = [base_list.copy()] * 4
#
# base_list[-1][0] = 1
# print(f'base_list {base_list}')
# print(new_list)

# from copy import deepcopy       # Жре багато памʼяті, запамʼятай, питають, краще не лізти, але іноді use
#
# base_list = [1, 2, 3, [True, False]]
#
# new_list = [deepcopy(base_list)] * 4
#
# base_list[-1][0] = 1
# print(f'base_list {base_list}')
# print(new_list)

# Вивчи методи на сайті!!!!!!!!!!