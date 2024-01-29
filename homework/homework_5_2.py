# Modified calculator

while True:
    number_1 = input('Enter the first number: ')
    if not number_1.isdigit():
        print('Undefined number! Try again.')
        continue
    number_1 = float(number_1)

    correct_actions = ['+', '-', '/', '*']
    action = input('Enter the operator: ')
    if action not in correct_actions:
        print('Unavailable operator! Try again.')
        continue

    number_2 = input('Enter the second number: ')
    if not number_2.isdigit():
        print('Undefined number! Try again.')
        continue
    number_2 = float(number_2)

    result = float

    if action == '+':
        result = number_1 + number_2
        print(result)
    elif action == '-':
        result = number_1 - number_2
        print(result)
    elif action == '*':
        result = number_1 * number_2
        print(result)
    elif action == '/' and number_2 == 0:
        result = str('Ділення на нуль неможливе!')
        print(result)
    else:
        result = number_1 / number_2
        print(result)
    var_cont = input('Do you want to continue? Y/N? ')
    if var_cont.lower() != 'y':
        print('Good bye!')
        break
