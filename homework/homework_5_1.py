# HomeWork Samohodskyi
import keyword
import string

user_string = input('Enter the string: ')

reserved_words = keyword.kwlist
punctuation = string.punctuation
# x = user_string.isidentifier()

if reserved_words or punctuation in user_string:
    print(False)
elif user_string.isnumeric():
    print(False)

else:
    print(True)

















# Calculator

# num_1 = float(input('Enter the first number:'))
# action =