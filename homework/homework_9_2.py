# Різниця між числами

def difference(*nums):
    if not nums:
        return 0
    num_list = list(nums)
    max_num = max(num_list)
    min_num = min(num_list)
    result = max_num - min_num
    return round(result, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
