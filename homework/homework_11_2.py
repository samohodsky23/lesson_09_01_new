def is_even(number):
    num_str = str(number)
    return not num_str[-1] in ('3', '5', '7', '9')



assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok')
