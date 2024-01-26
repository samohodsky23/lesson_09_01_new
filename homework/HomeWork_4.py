# Samohodskyi Homework
# Задача 1 | Написати програму, яка переміщає всі нулі в кінець списку

# my_list = [0, 1, 0, 12, 3]
# my_list = [0]
# my_list = [1, 0, 13, 0, 0, 0, 5]
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# print(my_list)
# my_list.sort(key=bool, reverse=True)
# print(my_list)

# Задача 2 | Задача з індексами

my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
# my_list = []

result = sum(my_list[::2]) * my_list[-1]        # Найкращий варіант
print(result)


# result = 0
#
# for item in my_list:
#     index = my_list.index(item)
#     if index % 2 == 0:
#         result += item
# if len(my_list):
#     result = result * my_list[-1]
# else:
#     result = 0
#
# print(result)
