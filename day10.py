
adapters=[] 
adapters.append(0)
with open('day10input.txt','r') as file:
         for data in file:
            adapters.append(int(data))
adapters.sort()
adapters.append(adapters[-1]+3)
                
def day10One():
    global adapters   
    ans1=0
    ans3=0
    for i in range(1,len(adapters)):
        if adapters[i]-adapters[i-1] == 1:
            ans1+=1
        if adapters[i]-adapters[i-1] == 3:
            ans3+=1
    print(ans1,ans3,ans1*ans3)
    
def createGraph():
    global adapters
    adapters_number= len(adapters)-1
    graph = {}
    for i in range(0,adapters_number-2):
        leafs = []
        for j in range(i+1,i+4):
            if adapters[j]-adapters[i] in [1,2,3]:
                leafs.append(adapters[j])
    
        graph.update({adapters[i]:leafs})
    
    for i in reversed(range(1,3)):
        leafs=[]
        for j in reversed(range(0,i)):   
            if adapters[adapters_number-j]-adapters[adapters_number-i] in [1,2,3]:
                leafs.append(adapters[adapters_number-j])
        graph.update({adapters[adapters_number-i]:leafs})
    
    return graph  

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def day10Two():
    global adapters
    ans = [1] + [0] * len(adapters)

    for i in range(len(adapters)):
        for j in range(i):
            if(adapters[i] - adapters[j] <= 3):
                ans[i] += ans[j]

    print(ans[len(adapters) - 1])
    
    """graph=createGraph()
    ans=find_all_paths(graph,0,adapters[-1])
    print(len(ans))"""
               
day10One()
day10Two()