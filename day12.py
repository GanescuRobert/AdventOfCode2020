data = []
with open('day12input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

def day12One():
    Dir_X = [0, 1, 0, -1]
    Dir_Y = [1, 0, -1, 0]
    dir_ = 1
    x,y=0,0
    for ins in data:
        command = ins[0]
        value = int(ins[1:])
        if command == 'N':
            y += value
        elif command == 'S':
            y -= value
        elif command == 'E':
            x += value
        elif command == 'W':
            x -= value
        elif command == 'L':
            dir_ = int(dir_+3*(value/90)) % 4
        elif command == 'R':
            dir_ = int(dir_+1*(value/90)) % 4
        elif command == 'F':
            x += Dir_X[dir_]*value
            y += Dir_Y[dir_]*value
    print(abs(x)+abs(y))
    
def day12Two():
    wx,wy=10,1
    x,y=0,0
    for ins in data:
        command = ins[0]
        value = int(ins[1:])
        if command == 'N':
            wy += value
        elif command == 'S':
            wy -= value
        elif command == 'E':
            wx += value
        elif command == 'W':
            wx -= value
        elif command == 'L':
            for pas in range(int(value/90)):
                wx,wy=-wy,wx            
        elif command == 'R':
             for pas in range(int(value/90)):
                wx,wy=wy,-wx   
        elif command == 'F':
            x+=value*wx
            y+=value*wy
           
    print(abs(x)+abs(y))
    
day12One()
day12Two()