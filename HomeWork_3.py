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
# Задача 2. Перемістити елемент у списку | Work in progress

list_1 = [12, 3, 4, 10]
list_2 = [1]
list_3 = []
list_4 = [12, 3, 4, 10, 8]

list_1.insert(0, list_1.pop(-1))
print(list_1)
print(list_2)
print(list_3)
list_4.insert(0, list_4.pop(-1))
print(list_4)
