# Question 1 Part 3
from copy import deepcopy

class Puzzle:
    def __init__(self, initial_state):
        self.initial = initial_state
        self.queue = []         #open list
        self.visited = []       #closed list

    def _find_pos(self, state):   #for checking position of blank tile
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:   
                    return i, j

    def _right(self, state, pos):   #for swapping tiles rightwards
        i, j = pos

        if j != 2:                                    #if it is not at rightmost position
            t = deepcopy(state)
            t[i][j], t[i][j+1] = t[i][j+1], t[i][j]   #swapping tiles rightwards
            return t
        else:
            return state

    def _left(self, state, pos):    #for swapping tiles leftwards
        i, j = pos

        if j != 0:                                    #if it is not at leftmost position
            t = deepcopy(state)
            t[i][j], t[i][j-1] = t[i][j-1], t[i][j]   #swapping tiles leftwards
            return t
        else:
            return state

    def _up(self, state, pos):    #for swapping tiles upwards
        i, j = pos

        if i != 0:                                    #if it is not at upmost position
            t = deepcopy(state)
            t[i][j], t[i-1][j] = t[i-1][j], t[i][j]   #swapping tiles upwards
            return t
        else:
            return state

    def _down(self, state, pos):    #for swapping tiles downwards
        i, j = pos

        if i != 2:                                    #if it is not at lowermost position
            t = deepcopy(state)
            t[i][j], t[i+1][j] = t[i+1][j], t[i][j]   #swapping tiles downwards
            return t
        else:
            return state

    def _enque(self, new_state):    #enqueuing in open list

        x = self._heu_mink(new_state)   #storing last value in a variable

        if len(self.queue) == 0:      #if queue is empty, add new state at first
            self.queue.append(new_state)

        elif x < self._heu_mink(self.queue[0]):   #if heuristic value of first element is less than x state, add it at first
            self.queue.insert(0, new_state)
        else:
            for i in range(1, len(self.queue)):  #if heuristic value of ith element is less than x state, add it at (i-1)th position
                if self._heu_mink(self.queue[i]) > x:
                    self.queue.insert(i-1, new_state)

    def _deque(self):   #put the state into visited list and then pop it out of open list
        self.visited.append(self.queue[0])

        ele = self.queue.pop(0)

        return ele

    def _heu_mink(self, state):   #heuristic function (Minkowski)
        val = 0

        for x in range(3):
            for i in range(3):
                q = state[x][i]

                for j in range(3):
                    for k in range(3):
                        if q == self.goal[j][k] and not (x == j and i == k):
                            val += pow(abs(x-j),3)+pow(abs(i-k),3)  #Minkowski Formula with power
                            break
        return pow(val,1/3)   #return Minkowski distance

    def _print(self, vis):    #print the existing state
        for k in range(len(vis)-1):
            x = vis[k]
            for i in range(3):
                for j in range(3):
                    print(x[i][j], end=" ")
                print("\n")
            print("  |")
            print("  |")
            print("  V")
        x = vis[-1]        #for goal state
        for i in range(3):
            for j in range(3):        
                print(x[i][j], end=" ")
            print("\n")

    def Solve(self, goal_state):             #main driver function
        current_state = deepcopy(self.initial)
        self.goal = goal_state
        if current_state == goal_state:  #if starting state is itself goal state
            return

        while 1:   #movement of tiles till goal state is reached
            pos = self._find_pos(current_state)

            new_state = self._down(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

            new_state = self._left(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

            new_state = self._right(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

            new_state = self._up(current_state, pos)
            if new_state != current_state:
                if new_state == goal_state:
                    print("Goal State Reached!!")
                    self.visited.append(new_state)
                    self._print(self.visited)
                    return
                else:
                    if new_state not in self.visited:
                        self._enque(new_state)

       

            if len(self.queue) > 0:             #if queue is greater than 0 dequeue it one by one
                current_state = self._deque()
            else:                               #if it is 0, goal state is not found
                print("Not Found!")
                return


if __name__ == '__main__':
    P = Puzzle([[2, 0, 3], [1, 8, 4], [7, 6, 5]])  #starting state
    P.Solve([[1, 2, 3], [8, 0, 4], [7, 6, 5]])     #goal state