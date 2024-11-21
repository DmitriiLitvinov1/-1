numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]
primes = []
not_primes = []
for i in numbers:
    for j in numbers:
        if i == 1:
            continue
        if j == 1:
            continue
        if i % j == 0 and i / j > 1:
            not_primes.append(i)
            break
        elif i / j == 1:
            primes.append(i)
            break
print('not_primes:', not_primes)
print('primes:', primes)