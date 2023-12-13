import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))


# game modes
RANDOM = 0
GREEDY_BFS = 1
MINIMAX = 2

# menu text
ABOUT_TEXT = '''
There are three different algorithms that the AI can use, which are described below.


1. Random:
On its turn the AI creates a list of currently available moves and picks an item from that list at random.

2. Greedy Best-First Search:
The Greedy BFS is a local search algorithm, meaning it has no ability to look into the future beyond immediately available moves. It works by assigning values to available moves, and always performing the move with the highest value operating under the greedy assumption that performing the highest value short-term move will lead to an efficient overall game-plan. In this checkers AI, the algorithm prioritizes taking pieces whenever available, then creating a king if possible, and lastly chasing the nearest enemy piece. If there are multiple possible moves available in the highest priority possible it will choose randomly from that priority move-list.

3. Minimax:
Generates a tree that contains all possible moves that are and could be available. The algorithm then assumes itself to be the “maximizer” player, a player that tries to make moves that maximize its chance of winning. It also labels the enemy player as the “minimizer”, who plays to minimize the maximizer’s chance at winning. Next the Minimax will simulate all possible optimal moves for both itself and the minimizer for their respective goals down the tree until reaching a terminal state (win/ loss) or until a specified depth. At this point, it will evaluate the current board, determine how well its score is maximized, and move on to the next simulation. After finding the best possible board state from the simulations, it backtracks and returns the next available move that will lead to the eventuality of a high-value board. This means it always returns the next optimal move. 
 
                    
The source code for our implementations of these algorithms, as well as for the rest of this project, can be found at github.com/poz123/aiproject1
'''
