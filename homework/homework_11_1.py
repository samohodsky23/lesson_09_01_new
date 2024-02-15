# Генератор простих чисел

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    if n == 1 or n == 0:
        return False
    else:
        return d * d > n


print(is_prime(29))


def prime_generator(end):
    num = 0
    while num <= end:
        if is_prime(num):
            yield num
        num += 1


print(next(prime_generator(10)))
print(next(prime_generator(10)))
print(list(prime_generator(29)))

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
