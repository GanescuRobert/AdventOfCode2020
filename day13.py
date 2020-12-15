

def day13One():
    with open('day13input.txt', 'r') as file:
        f = file.readlines()
        time = int(f[0])
        buses = [int(bus) for bus in f[1].split(',') if bus != 'x']

    busesTime = []
    for bus in buses:
        busesTime.append(bus-time % bus)

    earliestTime = min(busesTime)
    earliestBus = buses[busesTime.index(earliestTime)]

    print(earliestTime*earliestBus)



def day13Two():
    with open('day13input.txt', 'r') as file:
        f = file.readlines()
        buses = [(int(bus), i)
                 for i, bus in enumerate(f[1].split(','), 0) if bus != 'x']

    from sympy.ntheory.modular import crt
    
    b = []
    t = []
    for bus, time in buses:
        b.append(bus)
        t.append(time)
    ans = crt(b, t)
    print(ans[1]-ans[0])
    
    #https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    #https://www.geeksforgeeks.org/chinese-remainder-theorem-set-1-introduction/
    #https://www.geeksforgeeks.org/python-sympy-crt-method/

day13One()
day13Two()
