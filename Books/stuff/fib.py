# #! python3;

a = int(input())
def fib(n):
    d = [0, 1]
    for i in range(2, n+1):
        d.append(d[-1]+d[-2])
        print(d)
    return d[-1]

print(fib(a))


input()
