with open('day15input.txt', 'r') as file:
    data = [int(val) for val in file.read().split(',')]
def day15(position):
    value_idx = {}
    for idx, val in enumerate(data):
        value_idx[val] = idx
    data.append(0)
    while len(data) != position:
        curr = data[-1]
        prev_curr = value_idx.get(curr, -1)
        value_idx[curr] = len(data) - 1
        if prev_curr != -1:
            data.append(len(data) - 1 - prev_curr)
        else:
            data.append(0)

    print(data[-1])
day15(2020)
day15(30000000)

#
"""
while len(data)!=2020:
    curr = (data[-1], len(data)-1)
    if data.count(curr[0]) >1:
        for i in reversed(range(len(data)-1)):
            if data[i]==curr[0]:
                data.append(curr[1]-i)
                break
    else:
        data.append(0)

print(data[-1])
"""