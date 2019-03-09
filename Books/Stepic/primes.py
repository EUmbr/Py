import itertools


def primes():
    i = 2
    while True:
        var = 0
        for j in range(1, i+1):
            if i % j == 0:
                var += 1
        if var == 2:
            yield i
        i += 1

print(list(itertools.takewhile(lambda x: x <= 5, primes())))
