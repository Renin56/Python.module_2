# ВАРИАНТ 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True

primes = []
not_primes = []

for i in range(1, len(numbers) + 1):
    for k in range(2, i):
        if i % k == 0:
            is_prime = True
    if is_prime == False:
        primes.append(i)
    else:
        if i != 1:
            not_primes.append(i)
        is_prime = False

print('Primes: ', primes)
print('Not Primes: ', not_primes)

# ВАРИАНТ 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
del_ = 0

primes = []
not_primes = []

for i in range(1, len(numbers) + 1):
    for k in range(2, i):
        if i % k == 0:
            del_ = del_ + 1
    if del_ == 0:
        if i != 1:
            primes.append(i)
    else:
        not_primes.append(i)
        del_ = 0

print('Primes: ', primes)
print('Not Primes: ', not_primes)
