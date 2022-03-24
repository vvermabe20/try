 #Question 2
 
import sys
import copy

q = []       #open list
visited = [] #closed list

def compare(s,g):
    if s==g:  #if starting state is equal to goal state return 1 else 0
        return(1)
    else:
        return(0)

def find_pos(s):   #to find position of blank tile
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return([i,j])


def up(s,pos):   #for shifting the tile upwards
    
    i = pos[0]
    j = pos[1]
    
    if i > 0:   #if it is not at upmost position
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i-1][j]
        temp[i-1][j] = 0  #swapping tiles upwards
        return (temp)
    else:
        return (s)

    
def down(s,pos):   #for shifting the tile downwards
    
    i = pos[0]
    j = pos[1]
    
    if i < 2:     #if it is not at lowermost position
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0  #swapping tiles downwards
        return (temp)
    else:
        return (s)


def right(s,pos):   #for shifting the tile rightwards
    
    i = pos[0]
    j = pos[1]
    
    if j < 2:     #if it is not at rightmost position
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0  #swapping tiles rightwards
        return (temp)
    else:
        return (s)


def left(s,pos):   #for shifting the tile leftwards
    
    i = pos[0]
    j = pos[1]
    
    if j > 0:     #if it is not at leftmost position
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0  #swapping tiles leftwards
        return (temp)
    else:
        return (s)

def enqueue(s,val):   #enqueue the open list
    global q
    q = q + [(val,s)]

def heuristic(s,g):  #heuristic function
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    print(d)
    return d

                
def dequeue(g):       #enqueue visited list and dequeue open list
    
    global q
    global visited
    
    q.sort()
    visited = visited + [q[0][1]]
    
    elem = q[0][1]
    del q[0]
    return (elem)
    
def search(s,g):     #driver function
    
    curr_state = copy.deepcopy(s)
    if s == g:     #if starting state = goal state
        return

    global visited
    while(1):          #all branches for search tree
        
        pos = find_pos(curr_state)
        new = up(curr_state,pos)

        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g))
            

        new = down(curr_state,pos)

        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g))

        new = right(curr_state,pos)

        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g))

        new = left(curr_state,pos)

        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g))
        
        if len(q) > 0:
            curr_state = dequeue(g)
        else:
            print ("not found")
            return
        

def main():
    s = [[2,0,3],[1,8,4],[7,6,5]]   #starting state
    g = [[1,2,3],[8,0,4],[7,6,5]]   #end state
    global q
    global visited
    q = q 
    visited = visited + [s]
    
    search(s,g)
    
if __name__ == "__main__":
    main()
