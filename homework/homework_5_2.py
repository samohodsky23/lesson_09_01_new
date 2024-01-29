# Modified calculator

number_1 = float(input())

action = input()
correct_actions = ['+', '-', '/', '*']
while action not in correct_actions:
    print('Такої операції немає в списку! Спробуй ще.')
    action = input()

number_2 = float(input())

result = float


program_is_running = True



if action == '+':
    result = number_1 + number_2

elif action == '-':
    result = number_1 - number_2
elif action == '*':
    result = number_1 * number_2
elif action == '/' and number_2 == 0:
    result = str('Ділення на нуль неможливе!')
else:
    result = number_1 / number_2

print(result)

while program_is_running:

    answer = input('Бажаєте продовжити? \n'
                   'Введіть "y", якщо так і будь-який інший, якщо ні: ')
    if answer != 'y':
        program_is_running = False
    else: