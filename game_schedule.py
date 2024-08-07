import random
import copy
import math
def generate_freq_matrix(curr_state): #generates a 2D matrix that shows how many times a player has played other players
    freq_mat=[[0 for i in range(13)]for j in range(13)]
    lookup={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12}
    for row in range(13):
        for i in range(0,12,4):
            for j in range(i,i+4):
                for k in range(j+1,i+4):
                    x=lookup[curr_state[row][j]]
                    y=lookup[curr_state[row][k]]
                    freq_mat[x][y]+=1
                    freq_mat[y][x]+=1
    return freq_mat

def count_unique(curr_state): #Counts the number of unique matches played using a set
    temp = ['A','A','A','A']
    matches=set()
    for i in range(13):
        for j in range(12):
            
            if j%4==0 and j!=0:
                temp.sort()
                str=""
                for x in temp:
                    str=str+x
                matches.add(str)
            temp[j%4]=curr_state[i][j]
        temp.sort()
        str=""
        for x in temp:
            str=str+x
        matches.add(str)
    return len(matches)

def evaluate(curr_state): #returns a cost to denote how good/bad the state is
    freq=generate_freq_matrix(curr_state)
    cost=0
    for i in range(13):
        for j in range(13):
            if i!=j:
                if freq[i][j]==0: #If the current player has not played someone else atleast once, the cost is really high to encourage them to play
                    cost+=10000
                else:
                    cost+=min(abs(freq[i][j]-3),abs(freq[i][j]-4)) #Ideally wwe want around 3 or 4 games between two players, so anything other than that is given a cost depeending on how far it is from 3 or 4
    
    return [count_unique(curr_state),cost] #The first value indicates the number of unique games, the second value gives a cost based on how many times players play each other

def generate_states(curr_state): #randomly generates the next state
    x=random.randrange(13) #One row is chosen at random, and is shuffled
    random.shuffle(curr_state[x])
    
    
    #Another possible method is shuffling all rows, but here if the previous state had some good qualities, they are also lost, hence only one row shuffling is preferred
    #it is possible to shuffle only two players, but would take a longer time for convergence, hence the chosen method was found to be optimal
    #for i in curr_state:
    #     random.shuffle(i)
    return curr_state

def isbetter(new_value,curr_value): #Checks if the new state is better than the old state
    if new_value[0]>curr_value[0]:
        return True
    elif new_value[0] == curr_value[0]:
        return new_value[1]<curr_value[1]
    return False


def hill_climbing(curr_state):
    
    curr_value=evaluate(curr_state)
    new_value=curr_value.copy()
    new_state=None
    counter=0
    while True:
        count=0
        while not isbetter(new_value,curr_value): #Generates a better state than the current value
            new_state=generate_states(curr_state).copy()
            new_value=evaluate(new_state)
            count+=1
            if count>100 and new_value[0]==39 and new_value[1]<10000: #If even after trying for 100 times, if we are not able to generate a better state
                break                               #move on, only iff there are 39 unique games and everyone has played every other player atleast once
        if new_value[0]==39 and new_value[1]==0: #If the best case is reached, just exit and dont compute further
            return new_state
        else:
            curr_state=new_state.copy()
            curr_value=new_value.copy()
        counter+=1
        if counter > 2000: #Modify it to change the number of iterations, the more the iteration, the better the result
            return curr_state
    return curr_state
        
def random_restart(start_state):
    
    count=0
    ans=copy.deepcopy(start_state)
    ans_value=[0,0]
    while count<10:
        for i in start_state:
            random.shuffle(i)    
        temp=hill_climbing(copy.deepcopy(start_state))
        temp_value=evaluate(temp)
        if isbetter(temp_value,ans_value): #Stores the best answer generated so far
            ans=temp.copy()
            ans_value=temp_value.copy()
        count+=1
    return ans

def schedule(t):
    value=1e5*math.pi**(-t) #A time dependent decaying function
    return value

def simulated_annealing(curr_state):
    print("Simulated Annealing")
    t=0.01 #Time Step
    while True:
        T=schedule(t)
        if T<0.00001:
            return curr_state
        new_state=generate_states(copy.deepcopy(curr_state))
        curr_value=evaluate(curr_state)
        new_value=evaluate(new_state)
        #error=(((39-curr_value[0])*100000)+curr_value[1])-(((39-new_value[0])*100000)+new_value[1])
        error=(((39-curr_value[0])*500)+curr_value[1])-(((39-new_value[0])*500)+new_value[1]) #gave more penalty if the games are not unique, hence promotes unique games
        
        if error>0:
            curr_state=new_state.copy()
        else:
            prob=(math.exp((error)/T)) # Retunrs a value between 0 and 1
            rand=(random.random())
            if rand<prob:
                curr_state=new_state.copy()
        t=t+0.01
    return curr_state

def display_result(ans):
    lookup={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M'}
    for i in range(13):
        print("Bye for player ",lookup[i],": ",end="")
        for j in range(0,12,4):
           print("[",ans[i][j],ans[i][j+1],ans[i][j+2],ans[i][j+3],"] ",end="") 
        
        print("")

def summarize(ans):
    print("***Summary of matches played***")
    freq=generate_freq_matrix(ans)
    
    #Uncomment the lines to view a matrix that shows how many times each player has played with other
    # for i in freq:
    #     print(i)
    
    for i in range(13):
        lookup={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M'}
        print("Player ",lookup[i],"| ",end="")
        for j in range(13):
            if i==j:
                continue
            print(lookup[j],":",freq[i][j],end=", ")
        print("")
        
def main():
    start_state=[['B','C','D','E','F','G','H','I','J','K','L','M'],
                 ['A','C','D','E','F','G','H','I','J','K','L','M'],
                 ['A','B','D','E','F','G','H','I','J','K','L','M'],
                 ['A','B','C','E','F','G','H','I','J','K','L','M'],
                 ['A','B','C','D','F','G','H','I','J','K','L','M'],
                 ['A','B','C','D','E','G','H','I','J','K','L','M'],
                 ['A','B','C','D','E','F','H','I','J','K','L','M'],
                 ['A','B','C','D','E','F','G','I','J','K','L','M'],
                 ['A','B','C','D','E','F','G','H','J','K','L','M'],
                 ['A','B','C','D','E','F','G','H','I','K','L','M'],
                 ['A','B','C','D','E','F','G','H','I','J','L','M'],
                 ['A','B','C','D','E','F','G','H','I','J','K','M'],
                 ['A','B','C','D','E','F','G','H','I','J','K','L']]
    
    
    # Uncomment the line to implement random restart hill climbing
    # Random Restart Hill Climbing
    # print("Random Restart Hill Climbing")
    # ans=random_restart(start_state)
    #Sample output
    '''Bye for player  A : [ I C K H ] [ D E B J ] [ F L M G ] 
        Bye for player  B : [ F M H I ] [ L D E J ] [ K G A C ]
        Bye for player  C : [ L I A G ] [ E M K J ] [ H F D B ]
        Bye for player  D : [ H A C F ] [ J I G M ] [ L B E K ]
        Bye for player  E : [ K F C A ] [ B L I J ] [ D G M H ]
        Bye for player  F : [ A E M C ] [ D L H K ] [ G B J I ]
        Bye for player  G : [ J A B L ] [ K H M F ] [ C E I D ]
        Bye for player  H : [ G F J E ] [ K L M C ] [ D I B A ]
        Bye for player  I : [ B K C G ] [ A L H J ] [ D F E M ]
        Bye for player  J : [ M A K D ] [ C E I G ] [ B H L F ]
        Bye for player  K : [ M J H B ] [ L G I D ] [ C A F E ]
        Bye for player  L : [ B M C A ] [ K F J I ] [ H D E G ]
        Bye for player  M : [ I G H B ] [ J F C K ] [ L A E D ]
        ***Summary of matches played***
        Player  A | B : 3, C : 6, D : 3, E : 3, F : 3, G : 2, H : 2, I : 2, J : 2, K : 3, L : 4, M : 3,
        Player  B | A : 3, C : 2, D : 3, E : 2, F : 2, G : 3, H : 4, I : 4, J : 5, K : 2, L : 4, M : 2,
        Player  C | A : 6, B : 2, D : 1, E : 4, F : 4, G : 3, H : 2, I : 3, J : 1, K : 6, L : 1, M : 3, 
        Player  D | A : 3, B : 3, C : 1, E : 6, F : 2, G : 3, H : 4, I : 3, J : 2, K : 2, L : 4, M : 3,
        Player  E | A : 3, B : 2, C : 4, D : 6, F : 3, G : 3, H : 1, I : 2, J : 4, K : 2, L : 3, M : 3,
        Player  F | A : 3, B : 2, C : 4, D : 2, E : 3, G : 2, H : 5, I : 2, J : 3, K : 4, L : 2, M : 4,
        Player  G | A : 2, B : 3, C : 3, D : 3, E : 3, F : 2, H : 3, I : 6, J : 3, K : 2, L : 3, M : 3,
        Player  H | A : 2, B : 4, C : 2, D : 4, E : 1, F : 5, G : 3, I : 3, J : 2, K : 3, L : 3, M : 4,
        Player  I | A : 2, B : 4, C : 3, D : 3, E : 2, F : 2, G : 6, H : 3, J : 4, K : 2, L : 3, M : 2,
        Player  J | A : 2, B : 5, C : 1, D : 2, E : 4, F : 3, G : 3, H : 2, I : 4, K : 3, L : 4, M : 3,
        Player  K | A : 3, B : 2, C : 6, D : 2, E : 2, F : 4, G : 2, H : 3, I : 2, J : 3, L : 3, M : 4,
        Player  L | A : 4, B : 4, C : 1, D : 4, E : 3, F : 2, G : 3, H : 3, I : 3, J : 4, K : 3, M : 2, 
        Player  M | A : 3, B : 2, C : 3, D : 3, E : 3, F : 4, G : 3, H : 4, I : 2, J : 3, K : 4, L : 2,'''
    
   
    # This implements only first-choice hill climbing 
    print("Hill Climbing")
    ans=hill_climbing(start_state)
    
    display_result(ans)
    summarize(ans)

    #This implements simulated annealing
    ans=simulated_annealing(start_state)
    
    
    display_result(ans)
    
    summarize(ans)
           
if __name__ == "__main__":
    main()