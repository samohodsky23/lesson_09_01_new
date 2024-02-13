# def draw_rectangle(w, h, fill):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end='')
#
#     return None
#
# # draw_rectangle(7, 5, '*')
#
# # my_args = 7, 5, '*'
# # draw_rectangle(*my_args)
#
#
# my_args = [7, 5, '*']
# draw_rectangle(*my_args)


# def my_add(num_1, num_2):
#
#     return num_1 + num_2

# print(my_add(2, 3))
#
# my_math_adding = my_add
#
# print(my_math_adding(9, 8))

# def my_add(num_1, num_2):
#
#     return num_1 + num_2
#
# def my_mul(num_1, num_2):
#
#     return num_1 * num_2
#
# func_list = [my_add, my_mul]
# print(func_list)
#
# for func in func_list:
#     print(func(1, 3))

# choice = 1
#
# if choice == 1:
#     def my_func(n):
#         if n > 0:
#             return 1
#         else:
#             return 0
# else:
#     def my_func(n):
#         if n < 0:
#             return 1
#         else:
#             return 0
#
# print(my_func(10))

# def my_func(n):
#     if n > 0:
#         return 1
#     else:
#         return 0
#
# def my_func():
#     return 10
#
#
# #                             функція це обʼєкт! вона перезаписується
# # print(my_func(10))
# print(my_func.__name__)
# print(my_func.__module__)
#
# if __name__ == "__main__":
#     print('!!!!')


# def my_func(n):
#     """This func is doing something. IMPORTANT: """
#
#
#
#     if n > 0:
#         return 1
#     else:
#         return 0
#
#
#
# my_func()

# def my_func():
#     """"""

# print(str.find.__doc__)


# def my_add(num_1: int, num_2: int) -> int:
#     return num_1 + num_2
#
#
# print(my_add(2, 5))


# Рекурсія

# def fibo(n):
#     a = 0
#     b = 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
# print(fibo(10))

# def fibo(n):
#     # print(n)
#     if n in (1, 2):
#         return 1
#     return fibo(n-1) + fibo(n - 2)
#
# print(fibo(10))


# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result
#
#
# sequence = [0, 9, 8, -4, 2]
#
# res = my_filter(sequence, lambda x: x > 0)
#
# print(res)



#### map(), filter(), zip() #####

# value_str = '1234'
# int_nums = []
#
# for i in value_str:
#     int_nums.append(int(i))

# int_nums = map(int, '1234')
# print(int_nums)
# print(list(int_nums))

# def power(n):
#     return n ** 2
#
# numbers = [1, 2, 3, 4]
#
# power_numbers = map(power, numbers)
# print(numbers)
# print(list(power_numbers))
#
#
# power = lambda x: x ** 2

# filter()

# numbers = [1, 2, -4, 0, 3, 4]
# filter_nums = filter(lambda x: x > 0, numbers)
#
#
# print(list(filter_nums))

# zip()

numbers_1 = [1, -4, 0, 2, 3, 4]
numbers_2 = ('apple', 'red', 'true')
numbers_3 = [True, False]

for element in zip(numbers_1, numbers_2, numbers_3):
    print(element)






