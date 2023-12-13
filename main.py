# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
import pygame_menu
from checkers.constants import *
from checkers.game import Game
from minimax.algorithm import minimax
from randmove.algorithm import random_move
from gbfs.algorithm import gbfs_move

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

ai_algorithm = RANDOM


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def set_ai_algorithm(value, algorithm):
    global ai_algorithm
    ai_algorithm = algorithm


# actual game loop got moved to this function
def play_game():
    global ai_algorithm
    clock = pygame.time.Clock()
    game = Game(WIN)
    is_board_in_final_state = False
    run = True
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            new_board = None
            if ai_algorithm is RANDOM:
                new_board = random_move(game.get_board(), WHITE, game)
            elif ai_algorithm is GREEDY_BFS:
                # method call for greedy bfs move goes here (rn the game will just crash if you select this in options)
                new_board = gbfs_move(game.get_board(), WHITE, game)
            elif ai_algorithm is MINIMAX:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.winner() is not None:
                    run = False
                else:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        if game.winner() is not None:
            # update board for the last time
            if not is_board_in_final_state:
                game.update()
                is_board_in_final_state = True
            # display win text
            font = pygame.font.Font('freesansbold.ttf', 32)
            winner_text = ''
            if game.winner() is WHITE:
                winner_text = 'The AI won! Click to return to the main menu'
            elif game.winner() is RED:
                winner_text = 'You won! Click to return to the main menu'
            text = font.render(winner_text, True, WHITE, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            WIN.blit(text, text_rect)
            pygame.display.update()
        else:
            game.update()


def main():
    winner = None
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame_menu.Menu('Checkers AI', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)
    options_menu = pygame_menu.Menu('Options', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)
    about_menu = pygame_menu.Menu('About', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)

    # adding things to screens
    menu.add.button('Play', play_game)
    menu.add.button('Options', options_menu)
    menu.add.button('About', about_menu)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    options_menu.add.selector('AI Solving Algorithm: ',
                              [('Random', RANDOM), ('Greedy Best First Search', GREEDY_BFS), ('Minimax', MINIMAX)],
                              onchange=set_ai_algorithm)
    about_menu.add.label(ABOUT_TEXT, max_char=-1, font_size=20)

    menu.mainloop(surface)
    
    pygame.quit()


main()
