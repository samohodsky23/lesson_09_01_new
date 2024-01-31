# Ex. 2
# a_list, a_dict - для завдання "А"
# b_list - для завдання "Б"
# c_dict - для завдання "В"
# d_dict - для завдання "Г"

my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}

a_list = []
b_list = []

a_dict = {}
d_dict = my_dict_2.copy()

for key in my_dict_1:
    for key_2 in my_dict_2:
        if key == key_2:
            a_dict = {key}
            a_list = [a_dict]
            print(a_list)               # Вирішення завдання "А"

for key in my_dict_1:
    if key not in my_dict_2:
        b_dict = {key}
        b_list = [b_dict]
        print(b_list)                   # Вирішення завдання "Б"

# Вирішення завдання "В"
c_dict = dict(item for item in my_dict_1.items() if item[0] not in my_dict_2)


for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        d_dict[item[0]] = item[1]
    else:
        d_dict[item[0]] = [item[1], my_dict_2[item[0]]]     # Вирішення завдання "Г"


print(c_dict)
print(d_dict)