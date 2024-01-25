# weather = 'cold'
#
# match weather:
#     case 'cold':                         Класна альтернатива if/else, але повільніше!
#         print("It's cold")
#     case 'hot':
#         print("It's hot")
#     case 'raining':
#         print("It's raining")
#     case _:         # _:  -  else
#         print('Not weather')


############### list ################

# value_list = ['apple, orange, cherry, aaple']
#
# value_list.append('hello')      # Додає в кінець списку дані
# print(value_list)
#
# some_value = value_list.pop()                # Видаляє окремий обʼєкт у списку | () за замовчуванням останній обʼєкт
# print(some_value)
# print(value_list)
#
# value_list.reverse()        # Задом наперед
# print(value_list)
#
# # value_list.sort(reverse=False)      # Сортує за зазначиними умовами. Може по довжині, може по нумерації
# # value_list_1 = sorted(value_list, reverse=False)
#
# value_list.insert(5, 'oooo')        # Вставляє потрібний елемент в потрібне місце
# value_list.insert(5, 'oooo')
# value_list.insert(5, 'new')
# print(value_list)
# print(len(value_list))


# value_list = [1, 3, 9]      #88 bytes | for 3 nums
#
# value_list.append(2)    #88 bytes
# value_list.append(4)    #88 bytes             | Погугли, для швидкодії важливо
# value_list.append(5)    #122 bytes

################## Loop | Цикли | Петлі | Кільця ###################
# Бути обережним з Вайлом, бо може зациклитись програма
# while, for

# value_int = 0
# is_true = True

# while True:                  while за boolian
#     value_int += 1
#     print(value_int)

# while value_int < 10:        while за умовою
#     value_int += 1
#     print(value_int)

# while is_true:                while за прапором
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         is_true = False

#
# value_int = 0
# is_true = True

# while True:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         break               # перериває роботу всієї програми
# while is_true:
#     value_int += 1
#     print(value_int)
#     if value_int > 10:
#         is_true = False
# else:
#     print('The end')


# value_int = 0
# is_true = True
# while is_true:
#     value_int += 1
#
#     if value_int == 5:
#         continue
#
#     print(value_int)
#     if value_int > 10:
#         is_true = False
# else:
#     print('The end')


# for, for - else, range()

# some_str = "Hello"

# index = 0
# while index < len(some_str):
#     print(some_str[index])
#     index += 1

# for letter in some_str:
#     print(letter)


# range(5)   - (0-4) пʼятірка не включ.    Діапазон, послідовність
# range(2, 5) - (2-4)


# for i in range(2, 5, 2):        # остання 2-ка  -  крок
#     print(i)

# list_1 = [1, 2, 3, 4, 5]
# print(list_1[1:4:2])
# print(list_1[::-1])             # reverse робить, синтаксичний цукор

# for i in range(2, 5, 2):
#     print(i)
#     if i == 4:
#         break
# else:
#     print(111111)
#
# print('end')

# for number in range(5):
#     for num_2 in range(5):
#         if num_2 == 4:
#             break
#     print(number)
# else:
#     print("1111111")
#
# print("The end")

some_number = input('Number: ')
index = 0

while index < len(some_number):
    print(some_number[index])
    index += 1
# for letter in some_number:
#     print(letter)





