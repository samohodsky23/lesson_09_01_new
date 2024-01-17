# Samohodskyi HomeWork
# Задача 1. Найпростіший калькулятор | Done

# number_1 = int(input())
# action = input()
# number_2 = int(input())
# result = int
#
# if action == '+':
#     result = number_1 + number_2
# elif action == '-':
#     result = number_1 - number_2
# elif action == '*':
#     result = number_1 * number_2
# elif action == '/' and number_2 == 0:
#     result = str('Ділення на нуль неможливе!')
# else:
#     result = number_1 / number_2
#
# print(result)


#############################################################
# Задача 2. Перемістити елемент у списку | Done

my_list = [12, 3, 4, 10]        # Змінився
# my_list = [1]                 # Не змінився
# my_list = []                  # Не змінився
# my_list = [12, 3, 4, 10, 8]   # Змінився

if len(my_list) > 1:
    my_list.insert(0, my_list.pop())

print(my_list)