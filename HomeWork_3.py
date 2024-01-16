# Samohodskyi HomeWork
# Задача 1. Найпростіший калькулятор

number_1 = int(input())
action = str(input())
number_2 = int(input())

if action == '+':
    print(number_1 + number_2)
elif action == '-':
    print(number_1 - number_2)
elif action == '*':
    print(number_1 * number_2)
elif action == '/' and number_2 == 0:
    print('Ділення на нуль неможливе!')
else: print(number_1 / number_2)


