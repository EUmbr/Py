spotes = {'global': []}
spote_vars = {'global': []}


def create(name, parent):

    if parent in spotes:

        spotes[name] = parent
        spote_vars[name] = []


def add(name, var):
    if name in spotes:
        spote_vars[name].append(var)


def get(name, var):
    if name == 'global' and var not in spote_vars[name]:
        print('None')
    elif var in spote_vars[name]:
        print(name)

    else:
        get(spotes[name], var)


n = int(input())


for i in range(n):
    com = input().split()
    globals()[com[0]](com[1], com[2])
