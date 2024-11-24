import random

number = list(range(3, 21))
n = random.choice(number)

print(n)

results = []


def cripto():
    for i in range(1, n):
        for j in range(1, n):
            if i > j:
                continue
            elif j == i:
                continue
            if n % (i + j) == 0:
                results.extend([i, j])

    return results


cripto()

print('results:', *results)
