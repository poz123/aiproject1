import random
from copy import deepcopy


def gbfs_move(position, player, game):
    if position.winner() is not None or get_all_moves(position, player, game) is None:
        return position
    else:
        scores = []
        possible_moves = get_all_moves(position, player, game)
        for moves in possible_moves:
            score = 0
            score += (game.get_board().red_left - moves.red_left)*5
            score += (moves.white_kings - game.get_board().white_kings)*2
            score += 1
            scores.append(score)

        gbfs_choice = possible_moves[scores.index(max(scores))]
        return gbfs_choice


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():

            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board
