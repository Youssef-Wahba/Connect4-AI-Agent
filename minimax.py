import copy
import numpy as np

# Constants
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROWS = 6
COLS = 7
WINNING_LENGTH = 4


def isValidMove(board, col):
    return board[0][col] == EMPTY


def makeMove(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return


def getAllValidMoves(board):
    return [col for col in range(COLS) if isValidMove(board, col)]


def isWinner(board, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row][col + 1] == player
                and board[row][col + 2] == player
                and board[row][col + 3] == player
            ):
                return True

    # Check vertical
    for row in range(3):
        for col in range(7):
            if (
                board[row][col] == player
                and board[row + 1][col] == player
                and board[row + 2][col] == player
                and board[row + 3][col] == player
            ):
                return True

    # Check diagonal (bottomLeft to topRight)
    for row in range(3, 6):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row - 1][col + 1] == player
                and board[row - 2][col + 2] == player
                and board[row - 3][col + 3] == player
            ):
                return True

    # Check diagonal (topLeft to bottomRight)
    for row in range(3):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row + 1][col + 1] == player
                and board[row + 2][col + 2] == player
                and board[row + 3][col + 3] == player
            ):
                return True
    return False


def isBoardFull(board):
    return all(board[0][col] != EMPTY for col in range(COLS))


def evaluateBoardWinner(board):
    if isWinner(board, PLAYER_1):
        return 1
    elif isWinner(board, PLAYER_2):
        return -1
    else:
        return 0


def minimax(board, depth, maximizingPlayer):
    if (
        depth == 0
        or isWinner(board, PLAYER_1)
        or isWinner(board, PLAYER_2)
        or isBoardFull(board)
    ):
        return evaluateBoardWinner(board)
    validMoves = getAllValidMoves(board)
    if maximizingPlayer:
        value = float("-inf")
        bestColumn = np.random.choice(validMoves)
        for col in validMoves:
            nextBoard = copy.deepcopy(board)
            makeMove(nextBoard, col, PLAYER_1)
            evaluationScore = minimax(nextBoard, depth - 1, False)
            if evaluationScore > value:
                value = evaluationScore
                bestColumn = col
        return bestColumn
    # Minimizing player
    else:
        value = float("inf")
        bestColumn = np.random.choice(validMoves)
        for col in validMoves:
            nextBoard = copy.deepcopy(board)
            makeMove(nextBoard, col, PLAYER_2)
            evaluationScore = minimax(nextBoard, depth - 1, True)
            if evaluationScore < value:
                value = evaluationScore
                bestColumn = col
        return bestColumn


def makeBestMoveMinimax(board, depth):
    return minimax(board, depth, False)
