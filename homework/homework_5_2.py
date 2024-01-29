# Modified calculator


# correct_actions = ['+', '-', '/', '*']
# while action not in correct_actions:
#     print('Такої операції немає в списку! Спробуй ще.')
#     action = input()

# program_is_running = True

while True:
    number_1 = float(input('Enter the first number: '))

    action = input('Enter the operator: ')

    number_2 = float(input('Enter the second number: '))

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
    if input('Do you want to continue? Y/N?') != 'Y':
        break
print(result)

# while program_is_running:
#
#     answer = input('Бажаєте продовжити? \n'
#                    'Введіть "y", якщо так і будь-який інший, якщо ні: ')
#     if answer != 'y':
#         program_is_running = False
#     else: