a = []


def func(*data):
    for arg in data:
        a.append(arg)

func(1,2,3,4,5,6,6, 'f', 'ffd')
print(a)
