'''
randothellogame module

sets up a RandOthello game closely following the book's framework for games

RandOthelloState is a class that will handle our state representation, then we've 
got stand-alone functions for player, actions, result and terminal_test

Differing from the book's framework, is that utility is *not* a stand-alone 
function, as each player might have their own separate way of calculating utility


'''
import random
import copy

WHITE = 1
BLACK = -1
EMPTY = 0
BLOCKED = -2
SIZE = 8
SKIP = "SKIP"

class OthelloPlayerTemplate:
    '''Template class for an Othello Player

    An othello player *must* implement the following methods:

    get_color(self) - correctly returns the agent's color

    make_move(self, state) - given the state, returns an action that is the agent's move
    '''
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        '''Given the state, returns a legal action for the agent to take in the state
        '''
        return None

class RandomPlayer(OthelloPlayerTemplate):
    def __init__(self,mycolor):
        self.color=mycolor
    
    def get_color(self):
        return self.color
    
    def make_move(self,state):
        legals=actions(state)
        rand=random.randrange(len(legals))
        curr_move=legals[rand]
        return curr_move

class MinimaxPlayer(OthelloPlayerTemplate): 
    def __init__(self,mycolor,depth):
        self.color=mycolor
        self.max_depth=depth
    
    def getColor(self):
        return self.color
    
    def make_move(self,state):
        value,move=self.max_value(state,self.max_depth)
        return move
    
    def max_value(self,state,curr_depth):
        if terminal_test(state)==True:
            return self.utilityv1(state,self.color),None
        if curr_depth==0:
            return self.utilityv1(state,self.color),None
        v=-1e10 # Negative Infinity
        for move in actions(state):
            v2,a2=self.min_value(result(state,move),curr_depth-1)
            if v2>v:
              v=v2
              final_move=move
        return v,final_move
    
    def min_value(self,state,curr_depth):
        if self.color==BLACK:
            curr_color=WHITE
        else:
            curr_color=BLACK
        if terminal_test(state)==True:
            return self.utilityv1(state,curr_color),None
        
        if curr_depth==0:
            return self.utilityv1(state,curr_color),None 
        v=1e10 # Positive Infinity
        for move in actions(state):
            v2,a2=self.max_value(result(state,move),curr_depth-1)
            if v2<v:
              v=v2
              final_move=move
        return v,final_move
    
    def utilityv0(self,state,color):
        
        b=0
        w=0
        for i in range(8):
            for j in range(8):
                if state.board_array[i][j]==1:
                    
                    w+=1
                elif state.board_array[i][j]==-1:
                    
                    b+=1
        
        if color==WHITE:
            value=w-b
        else:
            value=b-w
        if terminal_test(state)==True:
            if b>w and color==BLACK:
                return 1e9
            elif w>b and color==WHITE:
                return 1e9
            elif w==b:
                return 0
            else:
                return -1e9
        return value      
        
    def utilityv1(self,state,color):
        weights=[[4,-3,2,2,2,2,-3,4],
                 [-3,-4,-1,-1,-1,-1,-4,-3],
                 [2,-1,1,0,0,1,-1,2],
                 [2,-1,0,1,1,0,-1,2],
                 [2,-1,0,1,1,0,-1,2],
                 [2,-1,1,0,0,1,-1,2],
                 [-3,-4,-1,-1,-1,-1,-4,-3],
                 [4,-3,2,2,2,2,-3,4]]
        bcount=0
        wcount=0
        b=0
        w=0
        # Weights Updation
        for i in range(8):
            for j in range(8):    
                
                if state.board_array[i][j]==-2:
                    if j==0:
                        weights[i][j+1]=4
                        weights[i][j+2]=-3
                    elif j==1:
                        weights[i][j+1]=4
                        weights[i][j+2]=-3
                    elif j==2:
                        weights[i][j-1]=4
                        weights[i][j+1]=4
                        weights[i][j+1]=-3
                    elif j==3:
                        weights[i][j-1]=4
                        weights[i][j-2]=-6
                        weights[i][j+1]=4
                        weights[i][j+2]=-2
                    elif j==4:
                        weights[i][j+1]=4
                        weights[i][j+2]=-6
                        weights[i][j-1]=4
                        weights[i][j-2]=-2
                    elif j==5:
                        weights[i][j+1]=4
                        weights[i][j-1]=4
                        weights[i][j-2]=-3
                    elif j==6:
                        weights[i][j-1]=4
                        weights[i][j-2]=-3
                    elif j==7:
                        weights[i][j-1]=4
                        weights[i][j-2]=-3
        
        # Value Calculation
        for i in range(8):
            for j in range(8):
                if state.board_array[i][j]==1:
                    wcount+=weights[i][j]
                    w+=1
                elif state.board_array[i][j]==-1:
                    bcount+=weights[i][j]
                    b+=1      
        value=0       
        if color==WHITE:
            value=(1*(wcount-bcount))
        else:
            value=(1*(bcount-wcount))
        
        
        if terminal_test(state)==True:
            if b>w and color==BLACK:
                return 1e9
            elif w>b and color==WHITE:
                return 1e9
            elif w==b:
                return 0
            else:
                return -1e9
        return value

class AplhabetaPlayer(OthelloPlayerTemplate):
    def __init__(self,mycolor,depth):
        self.color=mycolor
        self.max_depth=depth
    
    def getColor(self):
        return self.color
    
    def make_move(self,state):
        value,move=self.max_value(state,self.max_depth,-1e9,1e9)
        return move
    
    def max_value(self,state,curr_depth,alpha,beta):
        if terminal_test(state)==True:
            return self.utilityv1(state,self.color),None
        if curr_depth==0:
            return self.utilityv1(state,self.color),None
        v=-1e10 # Negative Infinity
        for move in actions(state):
            v2,a2=self.min_value(result(state,move),curr_depth-1,alpha,beta)
            if v2>v:
              v=v2
              final_move=move
              alpha=max(alpha,v)
              if v>= beta:
                  return v,final_move
        return v,final_move
    
    def min_value(self,state,curr_depth,alpha,beta):
        if self.color==BLACK:
            curr_color=WHITE
        else:
            curr_color=BLACK
        if terminal_test(state)==True:
            return self.utilityv1(state,curr_color),None
        
        if curr_depth==0:
            return self.utilityv1(state,curr_color),None 
        v=1e10 # Positive Infinity
        for move in actions(state):
            v2,a2=self.max_value(result(state,move),curr_depth-1,alpha,beta)
            if v2<v:
              v=v2
              final_move=move
              beta=min(beta,v)
              if v<=alpha:
                  return v,final_move
        return v,final_move
    
    def utilityv1(self,state,color):
        # This utility function gives weights to different locations on board. Corner pieces have high weights, but near corner pieces have negative weights, because if we place there, then opponent can take the corner piece
        weights=[[4,-3,2,2,2,2,-3,4],
                 [-3,-4,-1,-1,-1,-1,-4,-3],
                 [2,-1,1,0,0,1,-1,2],
                 [2,-1,0,1,1,0,-1,2],
                 [2,-1,0,1,1,0,-1,2],
                 [2,-1,1,0,0,1,-1,2],
                 [-3,-4,-1,-1,-1,-1,-4,-3],
                 [4,-3,2,2,2,2,-3,4]]
        bcount=0
        wcount=0
        b=0
        w=0
        # Weights Updation based on the blocked square
        for i in range(8):
            for j in range(8):    
                
                if state.board_array[i][j]==-2:
                    if j==0:
                        weights[i][j+1]=4
                        weights[i][j+2]=-3
                    elif j==1:
                        weights[i][j+1]=4
                        weights[i][j+2]=-3
                    elif j==2:
                        weights[i][j-1]=4
                        weights[i][j+1]=4
                        weights[i][j+1]=-3
                    elif j==3:
                        weights[i][j-1]=4
                        weights[i][j-2]=-6
                        weights[i][j+1]=4
                        weights[i][j+2]=-2
                    elif j==4:
                        weights[i][j+1]=4
                        weights[i][j+2]=-6
                        weights[i][j-1]=4
                        weights[i][j-2]=-2
                    elif j==5:
                        weights[i][j+1]=4
                        weights[i][j-1]=4
                        weights[i][j-2]=-3
                    elif j==6:
                        weights[i][j-1]=4
                        weights[i][j-2]=-3
                    elif j==7:
                        weights[i][j-1]=4
                        weights[i][j-2]=-3
        
        # Value Calculation
        for i in range(8):
            for j in range(8):
                if state.board_array[i][j]==1:
                    wcount+=weights[i][j]
                    w+=1
                elif state.board_array[i][j]==-1:
                    bcount+=weights[i][j]
                    b+=1      
        value=0       
        if color==WHITE:
            value=(1*(wcount-bcount))
        else:
            value=(1*(bcount-wcount))
            
        
        if terminal_test(state)==True:
            if b>w and color==BLACK:
                return 1e9
            elif w>b and color==WHITE:
                return 1e9
            elif w==b:
                return 0
            else:
                return -1e9
        return value    
        
    def utilityv0(self,state,color):
        # Simple utility function that counts the number of black and white pieces
        b=0
        w=0
        for i in range(8):
            for j in range(8):
                if state.board_array[i][j]==1:
                    
                    w+=1
                elif state.board_array[i][j]==-1:
                    
                    b+=1
        
        if color==WHITE:
            value=w-b
        else:
            value=b-w
        if terminal_test(state)==True:
            if b>w and color==BLACK:
                return 1e9
            elif w>b and color==WHITE:
                return 1e9
            elif w==b:
                return 0
            else:
                return -1e9
        return value
             
class HumanPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            display(state)
            if self.color == 1:
                print("White ", end='')
            else:
                print("Black ", end='')
            print(" to play.")
            print("Legal moves are " + str(legals))
            move = input("Enter your move as a r,c pair:")
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = int(move.split(',')[0]), int(move.split(',')[1])
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

class RandOthelloState:
    '''A class to represent an othello game state'''

    def __init__(self, currentplayer, otherplayer, board_array = None, num_skips = 0):
        if board_array != None:
            self.board_array = board_array
        else:
            self.board_array = [[EMPTY] * SIZE for i in range(SIZE)]
            self.board_array[3][3] = WHITE
            self.board_array[4][4] = WHITE
            self.board_array[3][4] = BLACK
            self.board_array[4][3] = BLACK
            x1 = random.randrange(8)
            x2 = random.randrange(8)
            self.board_array[x1][0] = BLOCKED
            self.board_array[x2][7] = BLOCKED
        self.num_skips = num_skips
        self.current = currentplayer
        self.other = otherplayer
              
def player(state):
    return state.current

def actions(state):
    '''Return a list of possible actions given the current state
    '''
    legal_actions = []
    for i in range(SIZE):
        for j in range(SIZE):
            if result(state, (i,j)) != None:
                legal_actions.append((i,j))
    if len(legal_actions) == 0:
        legal_actions.append(SKIP)
    return legal_actions

def result(state, action):
    '''Returns the resulting state after taking the given action

    (This is the workhorse function for checking legal moves as well as making moves)

    If the given action is not legal, returns None

    '''
    # first, special case! an action of SKIP is allowed if the current agent has no legal moves
    # in this case, we just skip to the other player's turn but keep the same board
    if action == SKIP:
        newstate = RandOthelloState(state.other, state.current, copy.deepcopy(state.board_array), state.num_skips + 1)
        return newstate

    if state.board_array[action[0]][action[1]] != EMPTY:
        return None

    color = state.current.get_color()
    # create new state with players swapped and a copy of the current board
    newstate = RandOthelloState(state.other, state.current, copy.deepcopy(state.board_array))

    newstate.board_array[action[0]][action[1]] = color
    
    flipped = False
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for d in directions:
        i = 1
        count = 0
        while i <= SIZE:
            x = action[0] + i * d[0]
            y = action[1] + i * d[1]
            if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
                count = 0
                break
            elif newstate.board_array[x][y] == -1 * color:
                count += 1
            elif newstate.board_array[x][y] == color:
                break
            else:
                count = 0
                break
            i += 1

        if count > 0:
            flipped = True

        for i in range(count):
            x = action[0] + (i+1) * d[0]
            y = action[1] + (i+1) * d[1]
            newstate.board_array[x][y] = color

    if flipped:
        return newstate
    else:  
        # if no pieces are flipped, it's not a legal move
        return None

def terminal_test(state):
    '''Simple terminal test
    '''
    # if both players have skipped
    if state.num_skips == 2:
        return True

    # if there are no empty spaces
    empty_count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == EMPTY:
                empty_count += 1
    if empty_count == 0:
        return True
    return False

def display(state):
    '''Displays the current state in the terminal window
    '''
    print('  ', end='')
    for i in range(SIZE):
        print(i,end='')
    print()
    for i in range(SIZE):
        print(i, '', end='')
        for j in range(SIZE):
            if state.board_array[j][i] == WHITE:
                print('W', end='')
            elif state.board_array[j][i] == BLACK:
                print('B', end='')
            elif state.board_array[j][i] == BLOCKED:
                print('X', end='')
            else:
                print('-', end='')
        print()

def display_final(state):
    '''Displays the score and declares a winner (or tie)
    '''
    wcount = 0
    bcount = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == WHITE:
                wcount += 1
            elif state.board_array[i][j] == BLACK:
                bcount += 1

    print("Black: " + str(bcount))
    print("White: " + str(wcount))
    if wcount > bcount:
        print("White wins")
    elif wcount < bcount:
        print("Black wins")
    else:
        print("Tie")

def play_game(p1 = None, p2 = None):
    '''Plays a game with two players. By default, uses two humans
    '''
    if p1 == None:
        p1 = HumanPlayer(BLACK)
    if p2 == None:
        p2 = HumanPlayer(WHITE)

    s = RandOthelloState(p1, p2)
    while True:
        action = p1.make_move(s)
        if action not in actions(s):
            print("Illegal move made by Black")
            print("White wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return
        action = p2.make_move(s)
        if action not in actions(s):
            print("Illegal move made by White")
            print("Black wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return
  
    
def main():
    
    p1=AplhabetaPlayer(BLACK,4)
    p2=RandomPlayer(WHITE)
    play_game(p1,p2)
    
    p1=RandomPlayer(BLACK)
    p2=AplhabetaPlayer(WHITE,4)
    play_game(p1,p2)

if __name__ == '__main__':
    main()
