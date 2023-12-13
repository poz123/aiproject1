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


1. Random: On its turn the AI creates a list of currently available moves and picks an item from that list at random.

2. Greedy Best-First Search: On its turn the AI creates a list of currently available moves and picks the move that it thinks has the highest value.

3. Minimax: On its turn the AI evaluates all currently available moves by recursively simulating what would happen if the opponent (you) played perfectly against it afterwards. Based on this evaluation, the AI takes the move it determines to be most likely to gain it a win in the future. 
 
                    
The source code for our implementations of these algorithms, as well as for the rest of this project, can be found at github.com/poz123/aiproject1
'''
