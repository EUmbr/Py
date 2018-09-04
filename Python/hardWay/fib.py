results = [0, 1] + [0] * 1000


def fib(x):
    if x > 1:
        if results[x] == 0:
        	results[x] = fib(x - 1) + fib(x - 2)
    return results[x]
    


print(fib(990))
