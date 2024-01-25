# Samohodskyi Homework
# nums = int(input())
# num_1 = nums // 1000
# num_2 = (nums // 100) % 10
# num_3 = (nums // 10) % 10
# num_4 = (nums // 1) % 10
# print(num_1)
# print(num_2)
# print(num_3)
# print(num_4)

# Вирішення задачи через divmod

nums = int(input('Please, add 4 digits: '))

num_1, l_1 = divmod(nums, 1000)
num_2, l_2 = divmod(l_1, 100)
num_3, l_3 = divmod(l_2, 10)
num_4, l_3 = divmod(l_3, 1)

print(num_1)
print(num_2)
print(num_3)
print(num_4)
