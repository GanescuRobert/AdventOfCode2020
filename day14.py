import re


def add_mem_by_mask(mask, p, v, mem):
    maskvalue = 0
    for j, bit in enumerate(reversed(mask)):
        valbit = v & (2 ** j)
        if bit == 'X':
            maskvalue += valbit
        elif bit == '1':
            maskvalue += 2 ** j

    mem[p] = maskvalue


def day14One():
    mem = {}
    with open('day14input.txt', 'r') as file:
        mask = ""
        p, v = [], []
        regex = r'\[(\d+)\] = (\d+)'
        for line in file:
            if 'mask' == line[0:4]:
                mask = line.split()[-1]
            elif 'mem' == line[0:3]:
                values = re.search(regex, line)
                p = int(values.group(1))
                v = int(values.group(2))
                add_mem_by_mask(mask, p, v, mem)

    print(sum(mem.values()))


def get_locations(mask, locations, p):
    mask = list(mask)
    p = format(p, 'b').zfill(36)
    ans = []
    for loc in locations:
        tempLoc = mask.copy()
        z = 0
        for i in range(len(tempLoc)):
            if tempLoc[i] == 'X':
                tempLoc[i] = str(loc[z])
                z += 1
            elif p[i] == '1':
                tempLoc[i] = '1'
        ans.append(int(''.join(tempLoc), 2))
    return ans


def decode(mask, p, v, mem):
    from itertools import product
    num_X = mask.count('X')
    combinations_by_X = list(product([0, 1], repeat=num_X))
    locations = get_locations(mask, combinations_by_X, p)
    for loc in locations:
        mem[loc] = v


def day14Two():
    mem = {}
    with open('day14input.txt', 'r') as file:
        mask = ""
        p, v = [], []
        regex = r'\[(\d+)\] = (\d+)'
        for line in file:
            if 'mask' == line[0:4]:
                mask = line.split()[-1]
            elif 'mem' == line[0:3]:
                values = re.search(regex, line)
                p = int(values.group(1))
                v = int(values.group(2))
                decode(mask, p, v, mem)

    print(sum(mem.values()))


day14One()
day14Two()
