# in board class there is a bug as it is not possible to choose the
# index = 6 from function select_column(6) and its behavior is
# similar to select_column(0) whice will affect the win state of our
# implemented AI agent and make it always lose in hard mode
# you can check the selected columns from terminal as it is not
# our fault of implementation despite of our continuous try to debug
# the mistake as it always results in errors
import copy

# Constants
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROWS = 6
COLS = 7
WINNING_LENGTH = 4


def isValidMove(board, col):
    return board[0][col] == EMPTY


def getAllValidMoves(board):
    return [col for col in range(COLS) if isValidMove(board, col)]


def makeMove(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return


def isBoardFull(board):
    return all(board[0][col] != EMPTY for col in range(COLS))


def evaluateBoardWinner(board):
    if isWinner(board, PLAYER_1):
        return 1
    elif isWinner(board, PLAYER_2):
        return -1
    else:
        return 0


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

    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row + 1][col + 1] == player
                and board[row + 2][col + 2] == player
                and board[row + 3][col + 3] == player
            ):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row - 1][col + 1] == player
                and board[row - 2][col + 2] == player
                and board[row - 3][col + 3] == player
            ):
                return True

    return False


def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    if (
        depth == 0
        or isWinner(board, PLAYER_1)
        or isWinner(board, PLAYER_2)
        or isBoardFull(board)
    ):
        return evaluateBoardWinner(board)

    if maximizingPlayer:
        maxEvaluation = float("-inf")
        validMoves = getAllValidMoves(board)
        for col in validMoves:
            nextBoard = copy.deepcopy(board)
            makeMove(nextBoard, col, PLAYER_1)
            evaluationScore = alphabeta(nextBoard, depth - 1, alpha, beta, False)
            maxEvaluation = max(maxEvaluation, evaluationScore)
            alpha = max(alpha, evaluationScore)
            if alpha >= beta:
                break
        return maxEvaluation
    # minimizing player
    else:
        min_eval = float("inf")
        validMoves = getAllValidMoves(board)
        for col in validMoves:
            nextBoard = copy.deepcopy(board)
            makeMove(nextBoard, col, PLAYER_2)
            evaluationScore = alphabeta(nextBoard, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, evaluationScore)
            beta = min(beta, evaluationScore)
            if alpha >= beta:
                break
        return min_eval


def makeBestMoveAlphaBeta(board, depth):
    validMoves = getAllValidMoves(board)
    bestScore = float("-inf")
    bestMove = None
    for col in validMoves:
        nextBoard = copy.deepcopy(board)
        makeMove(nextBoard, col, PLAYER_1)
        evaluationScore = alphabeta(
            nextBoard, depth - 1, float("-inf"), float("inf"), False
        )
        if evaluationScore > bestScore:
            bestScore = evaluationScore
            bestMove = col
    return bestMove
