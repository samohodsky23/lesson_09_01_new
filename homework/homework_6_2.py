# Ex. 2
# a_list, a_dict - для завдання "А"
# b_list - для завдання "Б"
# c_dict - для завдання "В"
# d_dict - для завдання "Г"

my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}

my_list_1 = []
my_list_2 = []

a_dict = {}
d_dict = {}

for key in my_dict_1:
    for key_2 in my_dict_2:
        if key == key_2:
            a_dict = {key}
            print(a_dict)

c_dict = dict(item for item in my_dict_1.items() if item[0] not in my_dict_2)


for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        d_dict[item[0]] = item[1]
    else:
        d_dict[item[0]] = [item[1], my_dict_2[item[0]]]


print(c_dict)
print(d_dict)