# HomeWork Samohodskyi №1
import keyword
import string

user_string = input('Enter the string: ')

reserved_words = keyword.kwlist

punctuation = string.punctuation
list_punctuation = list(punctuation)
list_punctuation.pop(26)

ident = user_string.isidentifier()

numeric = user_string.isnumeric()

is_space = False
is_punctuation = False
is_upper = False
first_num = False

for letter in user_string:
    if letter.isspace():
        is_space = True
    if letter in list_punctuation:
        is_punctuation = True
    if letter.isupper():
        is_upper = True

if user_string in reserved_words:
    print(False)

elif is_punctuation:
    print(False)

elif numeric:
    print(False)

elif user_string[0].isdigit():
    first_num = True
    print(False)

elif is_space:
    print(False)

elif is_upper:
    print(False)


else:
    print(True)
