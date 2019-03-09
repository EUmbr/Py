with open('data.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        with open('result.txt') as fr:
            tm = fr.read()

        with open('result.txt', 'w') as fw:
            print(line, tm, sep='\n', file=fw)
