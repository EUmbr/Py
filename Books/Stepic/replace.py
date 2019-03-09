s = input()
a = input()
b = input()
count = 0
while True:
    if s != s.replace(a, b):
        s = s.replace(a, b)
        count += 1
        if count > 1000:
                print('Impossible')
                break
    else:
        print(count)
        break
