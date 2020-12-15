import re
import queue


bag_list = []
with open('day7input.txt', 'r') as file:
    bagReg = r"(.*?) bags contain"
    bagsReg = r"((\d) (.*?)) bags?[,|\.]"
    for data in file:
        bag = re.findall(bagReg, data)
        bags = re.findall(bagsReg, data)
        bag_list.append((bag, bags))


def day7One():
    global bag_list

    ans = 0
    qu = queue.Queue()
    vis = []
    myBag = "shiny gold"
    qu.put(myBag)
    while(qu.empty() is False):
        myBag = qu.get()

        if myBag not in vis:
            vis.append(myBag)
        else:
            continue

        for bag, bags in bag_list:
            for b in bags:
                qn, q, n = b
                if(n == myBag):
                    qu.put(bag[0])
                    break

    print(len(set(vis))-1)


def day7Two():
    global bag_list

    ans = 1
    qu = queue.Queue()
    vis = []
    myBag = "shiny gold"
    qu.put(myBag)
   
    pathBags={}
    while(qu.empty() is False):
        myBag = qu.get()
        z=[]
        child = 0 
        for bag, bags in bag_list:
            if myBag == bag[0]:
                for b in bags:    
                    qn, q, n = b
                    child +=1
                    z.append((n,q))
                    qu.put(n)              
                break
        pathBags[myBag]=z
          
              
    for bag in pathBags:
        print(bag,pathBags[bag])
day7One()
day7Two()
