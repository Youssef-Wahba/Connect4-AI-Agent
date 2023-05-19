# in board class there is a bug as it is not possible to choose the
# index = 6 from function select_column(6) and its behavior is
# similar to select_column(0) whice will affect the win state of our
# implemented AI agent and make it always lose in hard mode
# you can check the selected columns from terminal as it is not
# our fault of implementation despite of our continuous try to debug
# the mistake as it always results in errors
from board import Board
import time
from alphaBeta import makeBestMoveAlphaBeta
from minimax import makeBestMoveMinimax

# GAME LINK
# http://kevinshannon.com/connect4/


def minimaxGame(depth):
    print("Minimax Game")
    print("Depth : ", depth)
    board = Board()
    game_end = False
    time.sleep(2)
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        # for debugging game board matrix
        print(game_board)
        generatedColumn = makeBestMoveMinimax(game_board, depth)
        # for debugging generated column by the agent
        print(generatedColumn)
        board.select_column(generatedColumn)
        time.sleep(2)
    print("Game ended check the game winner from the game on website")


def alphaBetaGame(depth):
    print("Alpha Beta Game")
    print("Depth : ", depth)
    board = Board()
    game_end = False
    time.sleep(2)
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        if game_end:
            break
        # for debugging game board matrix
        print(game_board)
        generatedColumn = makeBestMoveAlphaBeta(game_board, depth)
        # for debugging generated column by the agent
        print(generatedColumn)
        board.select_column(generatedColumn)
        time.sleep(2)
    print("Game ended check the game winner from the game on website")
