import time
import sys
from queue import PriorityQueue
class Node:
    state=None
    parent = None
    action=None  # Action applied to parent state to generate this node
    path_cost=0
    
    def __init__(self,state) -> None: #Initializes the variables
        self.state=state
    
    def actions(self): # Returns possible actions
        # D = Down
        # U= Up
        # L = Left
        # R = Right
        #nums=[int(x) for x in str(self.state)]
        pos=str(self.state).find("0")
        
        if pos==0:
            pos_actions=["L","U"]
        elif pos==1:
            pos_actions=["L","R","U"]
        elif pos==2:
            pos_actions=["R","U"]
        elif pos==3:
            pos_actions=["L","U","D"]
        elif pos==4:
            pos_actions=["R","L","U","D"]
        elif pos==5:
            pos_actions=["R","U","D"]
        elif pos==6:
            pos_actions=["L","D"]
        elif pos==7:
            pos_actions=["R","L","D"]
        elif pos==8:
            pos_actions=["R","D"]
          
        return pos_actions      
    
    def visualize(self): # Fucntion to visualize the state
        nums=[int(x) for x in str(self.state)]
        print("xxxxxxxxxxxxxxxxx")
        for i in range(3):
            for j in range(3):
                print("|","." if nums[(i*3)+j]== 0 else nums[(i*3)+j] ,end=" ")
            print("|")
            print("-------------")
            
    def __lt__(self, obj): # Avoids conflict while comparing two nodes. It is reached when the two nodes in priority queue have the same priority
        return self.path_cost < obj.path_cost

# Goal State
goal_state="123804765"

def child_node(node, action): #Function that generates a new node given the current state and action
    
    
    curr_state=list(node.state)
    pos=curr_state.index("0")
   
    if action == "U":
        curr_state[pos],curr_state[pos+3]=curr_state[pos+3],curr_state[pos]
    elif action == "D":
        curr_state[pos],curr_state[pos-3]=curr_state[pos-3],curr_state[pos]
    elif action == "L":
        curr_state[pos],curr_state[pos+1]=curr_state[pos+1],curr_state[pos]
    elif action == "R":
        curr_state[pos],curr_state[pos-1]=curr_state[pos-1],curr_state[pos]

    new_state=""
    for i in curr_state:
        new_state+=i
    new_node=Node(new_state)
    new_node.action=action
    return new_node

def result(node): #Function to print the result
    temp=node
    path=[]
    while temp.action != None:
       # temp.visualize()
        path.append(temp.action)
        
        temp=temp.parent
    path.reverse()
    for i in path:
        if i=="U":
            print("Up ",end=" ")
        elif i=="D":
            print("Down ",end=" ")
        elif i=="L":
            print("Left ",end=" ")
        elif i=="R":
            print("Right ",end=" ")
    print()

def breadth_first(start_node): #Breadth first search
    reached_states=[]
    reached_states.append(start_node.state)
    queue=[]
    queue.append(start_node)
    while len(queue)!=0:
        temp_node = queue.pop(0)
        if temp_node.state==goal_state:
            return temp_node
        actions=temp_node.actions()
        for i in actions:
            new_node = child_node(temp_node,i)
            new_node.path_cost=temp_node.path_cost+1
            new_node.parent=temp_node
             
            if new_node.state not in reached_states:
                reached_states.append(new_node.state)
                queue.append(new_node)
    
    return None

def is_cycle(check_state,node, depth): #Checks if there are any back edges to avoid cycles
    while depth:
        if node.parent == None:
            return False
        node=node.parent
        if node.state == check_state:
            return True
        depth-=1
    return False
        
def depth_limited(start_node,max_depth): #Depth limited search
    stack=[]
    stack.append(start_node)
    
    while len(stack)!=0:
        temp=stack.pop()
        if temp.state == goal_state:
            return 1,temp       # Returns 1 to indicate there is a solution
        if temp.path_cost > max_depth: #since path cost is uniform and taken as 1 here, it is equivalent to the depth
            continue
        for i in temp.actions():
            new_node = child_node(temp,i)
            new_node.path_cost=temp.path_cost+1
            new_node.parent=temp
            if not is_cycle(new_node.state,temp,max_depth-temp.path_cost): #It is sufficient to check till ancestors of max_depth - temp.path_cost because anything above that will be handled using the cycle limit. Although even without this it works, but this just avoids some computation
                stack.append(new_node)
                
    return 0,None
        
def iterative_deepening(start_node): #iterative deeping that calls depth limited search with new depth limits
    depth = 0
    while True: 
        flag,answer=depth_limited(start_node,depth)
        depth = depth +1
        if flag == 1:
            return answer

    return None
        
def num_wrong_tiles(curr_state): #Calculates the number of wrongly positioned tiles
    value=0
    for i in range(9):
        if curr_state[i]!=goal_state[i]:
            if curr_state[i]!="0":
                value+=1
    return int(value)

def manhattan_distance(curr_state): #calculates the sun of manhattan distance of all tiles from its current positon to goal position
    value=0
    for i in range(9):
        if curr_state[i]=="0":
            continue
        pos=goal_state.index(curr_state[i])
        x1=i//3
        y1=i%3
        x2=pos//3
        y2=pos%3
        value+=abs(x2-x1)+abs(y2-y1)
    
    return int(value)        
            
def astar(start_node,heuristic): # A star alogorithm
    reached_states=[]
    reached_states.append(start_node.state)
    queue=PriorityQueue() # Prioriy queue
    
    queue.put((heuristic(start_node.state),start_node))
    while queue.qsize()>0:
        temp = queue.get()
        temp_node=temp[1]
        if temp_node.state == goal_state:
            return temp_node
        actions=temp_node.actions()
        for i in actions:
            new_node = child_node(temp_node,i)
            new_node.path_cost=temp_node.path_cost+1
            new_node.parent=temp_node
             
            if new_node.state not in reached_states: # Since the heuristic is admissible, the first time a node is reached, it is optimal.
                reached_states.append(new_node.state)
                fn=new_node.path_cost+heuristic(new_node.state)
                
                queue.put((fn,new_node))
                
                
    return None 
def main():
    #Takes input and stores it in a string
    curr_state=sys.argv[1]
    start_node=Node(curr_state)
    
    # # Breadth first search
    start_time=time.time()
    answer_bfs=breadth_first(start_node)
    end_time=time.time()
    if answer_bfs !=None:
        result(answer_bfs)
    else:
        print("No Solution")
    print("BFS took ",end_time-start_time," seconds")
    
    
    # # Iterative Deepening
    start_time=time.time()
    answer_id=iterative_deepening(start_node)
    end_time=time.time()
    if answer_id != None:
        result(answer_id)
    else:
        print("No Solution")
    print("IDDFS took ",end_time-start_time," seconds")
    
    
    # A star with number of wrong tiles as heuristic
    start_time=time.time()
    answer_nwt=astar(start_node,num_wrong_tiles)
    end_time=time.time()
    if answer_nwt !=None:
        result(answer_nwt)
    else:
        print("No Solution")
    print("Astar with number of wrong tiles heuristic took ",end_time-start_time," seconds")
    
    
    #A star as manhattan distance as heuristic
    start_time=time.time()
    answer_md=astar(start_node,manhattan_distance)
    end_time=time.time()
    if answer_md !=None:
        result(answer_md)
    else:
        print("No Solution")
    print("Astar with number of manhattan distance heuristic took ",end_time-start_time," seconds")
    
    
    
    


if __name__=="__main__":
    main()
            