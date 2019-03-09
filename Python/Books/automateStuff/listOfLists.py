import os
import psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)

def printTable(data):
    colWidth = [0] * len(data)
    for i in range(len(data)):
        colWidth[i] = len(sorted(data[i], key=len)[-1])
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].ljust(colWidth[j]), end=' ')
        print()


dataTable = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goooooose']]

printTable(dataTable)
