# Запиши в домашку 3 калькулятор через match case.

######### str | str methods(lower, upper, capitalize, isalpha, rfind, replace, starwith) ########

# value_str = 'hello'
# print(id(value_str))              String не змінна!
# value_str = 'hello!'
# print(id(value_str))

# value_str = 'hello'
# index = 0
# print(value_str[::2])
# print(value_str[10:])

# while index < len(value_str):
#     index += 1
#     print(index)

# for index in range(len(value_str)):           це вірне
#     print(index)

#
# for index, letter in enumerate(value_str):            зручніше і швидше
#     print(index, letter)


# value_list = [1, 2, 3]
# value_str = str(value_list)
# print(value_str, type(value_str))

# value_str = "hello"
# value_str_1 = value_str.lower()
# value_str_2 = value_str.upper()
# value_str_3 = value_str.capitalize()        # З великої літери
# value_str_4 = value_str.title()
# print(value_str_4)

# print(value_str, id(value_str))
# print(value_str_1, id(value_str_1))
# print(value_str_2, id(value_str_2))
# print(value_str_3, id(value_str_3))

# value_float = '12w'
# value = ""
# # value_is_digit = value_float.isdigit()
#
#
# for letter in value_float:
#     if letter.isdigit():                      Для другої задачки підказка!!
#         value += letter
# # print(value_float, value_is_digit)
#
# print(value)

# value_float = 'helloeeeellellleeeee'
# # method = value_float.find('l')
# # method_2 = value_float.rfind('l')
# # print(method)
# # print(method_2)
# # print(value_float[method +1:])
#
# method = value_float.index('l')
# print(method)

# method = value_float.find('p')          #якщо немає елементу в змінній - видає -1!!! no error!!!


#### split() ####

# value_float = "Hello/World/kkk"
# value = "C/Documents/kkk.txt"
# some_method = value.split(".")
# # join()
# some_method[-1] = "jpeg"
# result = ".".join(some_method)
# print(some_method)
# print(result)


# value = 'c/Documents/kkk.png.png.png.png'
# result = value.replace(".png", ".jpeg", 1)
# index = result.find('.png')
# result_1 = result[:index]
# print(result)
# print(result_1)

# strip()
# rsrip()

# value = '       hello           '

# result = value.strip()          # видаляє всі пробіли зайві | чистить рядок
# result_1 = value.rstrip()       # видаляє пробіли справа
# result_2 = value.lstrip()       # видаляє пробіли зліва

# print(value)
# print(result)
# print(result_1)
# print(result_2)


######## ASCII ########

# value = 'hello'         # тут буква "о" англійська
# value_1 = 'hellо'       # тут буква "о" українська
# # в пайтоні кожна буква має різне значення

# value = ""
# # print(ord(value))
# # print(chr(100))
#
# for index_of_character in range(ord('a'), ord('z')+1):
#     value += chr(index_of_character)
#     # print(chr(index_of_character), index_of_character)
# print(value)

####### спробуй зробити шифр цезаря. Задача з зірочкою по бажанню | import this

# value = "a"
# print(ord(value))
# value = chr(ord(value)+1)
# print(value)



