#### Функції. Генератори, декоратори ############

# Generator
#
# gen = range(5)
# print(gen)
# print(type(gen))
#
# import sys
# #
# # print(sys.getsizeof(range(500)))    # range компактний, і в незалежності яке там число
# # # він завжди буде однаковий
#
# gen_list = list(gen)
# print(gen_list)


# def add_one(num):
#     return num + 1
#
# def count(start, func):
#     while True:
#         yield start
#         start = func(start)
#
#
# counter = count(0, add_one)
# # print(counter)
# # print(sys.getsizeof(counter))
#
# print(next(counter))
#
# print(next(counter))
#
# print(next(counter))

# def some_gen():
#     yield 42
#
# gen = some_gen()
# print(list(gen))
# print(list(gen))


# def s_gen():
#     x = 1
#     while x > 0:
#         print('x > 0')
#         x = yield 45
#         print(f'Received: {x}')
#         if x is None:
#             x = 0
#
# new_gen = s_gen()
# print(next(new_gen))
# new_gen.send(90)
# print(next(new_gen))

import sys

# value_list = [i * 2 for i in range(1000)]
#
# list_generator = (i * 2 for i in range(10))
#
# # print(value_list)
# # print(list_generator)
# print(sys.getsizeof(value_list))
# print(sys.getsizeof(list_generator))

# далі дивись в відео (!!!)
























