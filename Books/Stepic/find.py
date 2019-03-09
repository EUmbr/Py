s = 'abababa'
t = 'abc'
count = 0
index = 0

while True:
    if s.find(t, index) != -1:
        count += 1
        index = s.find(t, index) + 1
    else:
        print(count)
        break
