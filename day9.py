from queue import Queue

def day9One():
    with open('day9input.txt','r') as file:
        numbers = Queue()
        for data in file:
            value = int(data)
            
            if numbers.qsize() == 25:
                from itertools import combinations
                
                ans=combinations(list(numbers.queue),2)

                sum_condition = False
                for a,b in ans:
                    if a+b == value:
                        sum_condition = True
                
                if sum_condition:
                    numbers.get()
                else:
                    print(value) #! Part 1 answer
                    return value
                
            numbers.put(value)

def day9Two():
    value = day9One()
    
    with open('day9input.txt','r') as file:
        numbers = []
        for data in file:
            if int(data) == value:
                break
            numbers.append(int(data))
            
    ans=0
    for i in range(len(numbers)):
        sum_range=numbers[i]
        for j in range(i+1,len(numbers)):
            sum_range+=numbers[j]
            if sum_range == value:
                temp = numbers[i:j+1]
                v_max,v_min = max(temp),min(temp)
                print(v_max+v_min) #! Part 2 answer
                return      
            if sum_range > value:
                break  
    
day9Two()