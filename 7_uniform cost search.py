
from queue import PriorityQueue
inp={"A":{"S":1,"G":10},"B":{"S":5,"G":5},"C":{"S":15,"G":5},"G":{"A":10,"B":5,"C":5},"S":{"A":1,"B":5,"C":15}}
init="A"
goal="G"
curr=init
visited=[init]
inp_sorted={}
mp={}#used for backtracking
for curr in inp:
    pq=PriorityQueue()
    d=inp[curr]
    for i in d.keys():
        pq.put((d[i],i))
    l=[]
    while(pq.empty()==False):
        l.append(pq.get()[1])
    inp_sorted[curr]=l
#print(inp_sorted)
curr=init
path=init
cost=0
while curr!=goal:
    l=[]
    l=inp_sorted[curr]
    x="-1"
    while len(l)>0 and (l[0] in visited):
        l.pop(0)
    if(len(l)==0):
        if(mp[curr]==init):
            print("Infinite Loop")
            exit(0)
        else:
            #backtrack
            cost+=inp[curr][mp[curr]]
            path+="->"
            path+=mp[curr]
            curr=mp[curr]
            continue
    x=l[0]
    mp[x]=curr
    l.pop(0)
    visited.append(x)
    inp_sorted[curr]=l
    path+="->"
    path+=x
    cost+=inp[curr][x]
    curr=x
    if(x==goal):
        print("Path = ",path," Cost = ",cost)
        exit(0)