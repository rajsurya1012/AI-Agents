import pygame
import sys
class BaghChal:
    def __init__(self):
        # Pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Bagh Chal")

        # Create a 5x5 board filled with None
        self.board = [[None for _ in range(5)] for _ in range(5)]

        # Place the tigers at the four corners
        self.board[0][0] = 'T'
        self.board[0][4] = 'T'
        self.board[4][0] = 'T'
        self.board[4][4] = 'T'

        # Initialize the number of goats
        self.goats = 20
        self.goats_captured = 0
        
        self.current_player = 'G'
        
        self.game_winner=None

    def draw_board(self):
    # Draw the grid
        for i in range(6):
            pygame.draw.line(self.screen, (255, 255, 255), (i*120, 0), (i*120, 600)) # Vertical lines
            pygame.draw.line(self.screen, (255, 255, 255), (0, i*120), (600, i*120)) # Horizontal lines

        # Draw the tigers
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == 'T':
                    pygame.draw.circle(self.screen, (255, 0, 0), (i*120+60, j*120+60), 50)
        
        # Draw the goats
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == 'G':
                    pygame.draw.circle(self.screen, (0, 0, 255), (i*120+60, j*120+60), 50)
    def update_game_state(self):
    # Redraw the board and update the display
        self.draw_board()
        pygame.display.flip()  
              
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.game()
            self.draw_board()
            pygame.display.flip()

        pygame.quit()
    
    def game(self):
        #while(self.end_state()==False):
        if self.current_player == 'G':
            if self.goats > 0:
                # If there are still goats to be placed
                print("Goat's turn. Choose a square to place a new goat.")
                row, col = self.get_move()
                self.goats -= 1
            else:
                # If all goats have been placed, they can move
                print("Goat's turn. Choose a goat to move.")
                start_row, start_col = self.get_move()
                print("Choose a square to move to.")
                end_row, end_col = self.get_move()
            
        else:
            # Code for the tigers' turn
            print("Tiger's turn. Choose a tiger to move.")
            start_row, start_col = self.get_move()
            print("Choose a square to move to.")
            end_row, end_col = self.get_move()

        # Switch to the other player if move is valid
        if valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = None
            # Account for tigers capturing goats
            
                        
            self.current_player = 'T' if self.current_player == 'G' else 'G'
            self.update_game_state()
        else:
            print("Invalid move. Try again.")
                
        # Display Winner
        if self.game_winner == 'T':
            print("Tigers win!")
        else:
            print("Goats win!")
            
        if self.game_winner is not None:
            font = pygame.font.Font(None, 36)
            text = font.render(f'Player {self.game_winner} wins!', True, (255, 255, 255))
            self.screen.blit(text, (20, 20))
            pygame.display.flip()

            # Wait for a click before ending the program
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        sys.exit()
    
    def get_move(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 120
                    col = x // 120
                    if self.board[row][col] == self.current_player:
                        return (row, col)
                    else :
                        print("Invalid move. Try again.")
                        continue   
    
    def valid_move(self, start_row, start_col, end_row, end_col,current_player=None):
        # Check if the start and end squares are on the board
        if current_player is None:
            current_player = self.current_player
        if not (0 <= start_row < 5 and 0 <= start_col < 5 and 0 <= end_row < 5 and 0 <= end_col < 5):
            return False

        # Check if the start square contains the current player's piece
        if self.board[start_row][start_col] != current_player:
            return False

        # Check if the end square is empty
        if self.board[end_row][end_col] is not None:
            return False

        if self.current_player == 'G':
            # Goats can only move to adjacent squares
            if abs(start_row - end_row) > 1 or abs(start_col - end_col) > 1:
                return False
        else:
            # Tigers can move to adjacent squares or jump over goats
            if abs(start_row - end_row) > 2 or abs(start_col - end_col) > 2:
                return False
            if abs(start_row - end_row) == 2 or abs(start_col - end_col) == 2:
                # If the tiger is jumping, there must be a goat in between
                if self.board[(start_row + end_row) // 2][(start_col + end_col) // 2] != 'G':
                    return False

        return True
            
    def end_state(self):
        # Check if 5 or more goats have been captured
        if self.goats_captured >= 5:
            self.game_winner='T'  # Tigers win

        # Check if the tigers can make a move
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == 'T':
                    # Check all adjacent squares and jumps
                    
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (1, 1), (-1, 1), (1, -1), (-2, -2), (2, 2), (-2, 2), (2, -2)]:
                        new_row, new_col = row + dr, col + dc
                        
                        if self.valid_move(row, col, new_row, new_col,'T'):
                            return False  # Game continues

        self.game_winner='G' # Goats win
        return True  
    
if __name__ == "__main__":
    game = BaghChal()
    game.run()