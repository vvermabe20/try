from queue import PriorityQueue
def row(value):
    if(value>-1 and value<3):
        return 0
    if(value>2 and value<6):
        return 1
    if(value>5 and value<9):
        return 2
def column(value):
    if(value==0 or value==3 or value==6):
        return 0
    if(value==1 or value==4 or value==7):
        return 1
    if(value==2 or value==5 or value==8):
        return 2
def h(c,g):
    man=0
    for i in range(1,9):
        a=c.find(str(i))
        b=g.find(str(i))
        x1=row(a)
        x2=row(b)
        y1=column(a)
        y2=column(b)
        man+=abs(x1-x2)+abs(y1-y2)
    return man

#-------------------------------------------------------------------------------------

def left(s,pos):
    ss=""
    for i in s:
        if i==s[pos-1]:
            ss+=s[pos]
        elif i==s[pos]:
            ss+=s[pos-1]
        else:
            ss+=i
    return ss
def right(s,pos):
    ss=""
    for i in s:
        if i==s[pos+1]:
            ss+=s[pos]
        elif i==s[pos]:
            ss+=s[pos+1]
        else:
            ss+=i
    return ss
def up(s,pos):
    ss=""
    for i in s:
        if i==s[pos-3]:
            ss+=s[pos]
        elif i==s[pos]:
            ss+=s[pos-3]
        else:
            ss+=i
    return ss
def down(s,pos):
    ss=""
    for i in s:
        if i==s[pos+3]:
            ss+=s[pos]
        elif i==s[pos]:
            ss+=s[pos+3]
        else:
            ss+=i
    return ss


initial=input("Input initial state as a string non space separated where empty block is 0\n")
goal=input("Input initial state as a string non space separated where empty block is 0\n")
que=[initial]
que2=[]
pq=PriorityQueue()
mp={}
c=0
while (len(que)>0):
    curr=que[0]
    if(curr==goal):
        break
    pos=int(curr.find('0'))
    if(pos!=0 and pos!=3 and pos!=6):
        c+=1
        res=left(curr,pos)
        if res not in mp.keys():
            mp[res]=curr
            pq.put((h(res,goal),res))
    if(pos!=2 and pos!=5 and pos!=8):
        c+=1
        res=right(curr,pos)
        if res not in mp.keys():
            mp[res]=curr
            pq.put((h(res,goal),res))
    if(pos!=6 and pos!=7 and pos!=8):
        c+=1
        res=down(curr,pos)
        if res not in mp.keys():
            mp[res]=curr
            pq.put((h(res,goal),res))
    if(pos!=0 and pos!=1 and pos!=2):
        c+=1
        res=up(curr,pos)
        if res not in mp.keys():
            mp[res]=curr
            pq.put((h(res,goal),res))
    que.pop(0)
    if(pq.empty()==False):
        que.append(pq.get()[1])
    lst=[]
    while(pq.empty()==False):
        lst.insert(0,pq.get()[1])
    while(len(lst)>0):
        que2.insert(0,lst[0])
        lst.pop(0)
    if(len(que)==0 and len(que2)>0):
        que.append(que2[0])
        que2.pop()
print("Reached")
curr=goal
result=[goal]
while curr!=initial:
    result.insert(0,mp[curr])
    curr=mp[curr]
print("Reached")
for i in result:
    print(i[0:3],end=" ")
print("\n",end="")
for i in result:
    print(i[3:6],end=" ")
print("\n",end="")
for i in result:
    print(i[6:9],end=" ")