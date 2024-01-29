# Ex. 1

my_list = [{'name': 'John', 'age': 15},
           {'name': 'Jack', 'age': 45},
           {'name': 'Charles', 'age': 15},
           {'name': 'Arthur', 'age': 39},
           {'name': 'Samuele', 'age': 60}
           ]

min_age = float(130)
max_len = float()
over = int()

for person in my_list:
    max_int = 100
    if person['age'] < min_age:
        min_age = person['age']
    if len(person['name']) > max_len:
        max_len = len(person['name'])
    over += person['age'] / len(my_list)

young_list = [p['name'] for p in my_list if p['age'] == min_age]
long_list = [p['name'] for p in my_list if len(p['name']) == max_len]

print(young_list)
print(long_list)
print(over)

