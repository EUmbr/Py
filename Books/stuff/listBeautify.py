def beauty(list):
    return ', '.join(map(str, list[:-1])) + f' and {list[-1]}'


print(beauty([i**3 for i in range(10)]))

input()