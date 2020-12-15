



def day6One():
    
    groups = []
    group = set()
    with open('day6input.txt') as file:
        for data in file:
            
            if data == '\n':
                groups.append(list(group))
                group.clear()
            else:
                data = data.replace('\n','')
                for ch in data:
                    group.update(ch)
    
    ans=0
    for g in groups:
        ans+=len(g)
    print(ans)
    
def day6Two():
    apparance = {}
    with open('day6input.txt') as file:
        ans=0
        count=0
        for data in file:       
            if data == '\n':
                for key in apparance:
                    if apparance[key]==count:
                        ans+=1
                apparance.clear()
                count=0
            else:
                count+=1
                data = data.replace('\n','')
                for ch in data:
                    if ch not in apparance: 
                        apparance[ch]=1
                    else:
                        apparance[ch] = apparance[ch] + 1
    print(ans)

day6One()
day6Two()