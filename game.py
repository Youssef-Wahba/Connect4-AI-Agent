from board import Board
import time
from alphaBeta import makeBestMoveAlphaBeta
from minimax import makeBestMoveMinimax

# GAME LINK
# http://kevinshannon.com/connect4/


def minimaxGame(depth):
    board = Board()
    game_end = False
    time.sleep(2)
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        if game_end:
            break
        # for debugging game board matrix
        print(game_board)
        generatedColumn = makeBestMoveMinimax(game_board, depth)
        # for debugging generated column by the agent
        print(generatedColumn)
        board.select_column(generatedColumn)
        time.sleep(2)
    print("Game ended check the game winner from the game on website")


def alphaBetaGame(depth):
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


# 1 5 7
def main():
    board = Board()
    game_end = False
    time.sleep(2)
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        if game_end:
            break
        board.select_column(6)
        time.sleep(2)
    print("Game ended check the game winner from the game on website")


if __name__ == "__main__":
    main()
