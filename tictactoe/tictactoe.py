"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    the board is represented as a list of lists
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    X always moves first (i.e., when board is in initial state)
    """
    # initialize X and O count to 0
    xCount = 0
    oCount = 0

    # iterate over every row (i.e., list) of the game board
    for row in board:
        # iterate over every item in row (i.e., X, O, or EMPTY)
        # and keep track of how many Xs and Os are on the game board
        for item in row:
            if item == 'X':
                xCount += 1
            if item == 'O':
                oCount += 1

    # if amount of X and O are equal, it is X's turn. Otherwise, it is O's turn
    if xCount == oCount:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0 # row
    j = 0 # cell
    setOfMoves = set()
    # iterate over every row (i.e., list) of the game board
    for row in board:
        # iterate over every item in row (i.e., X, O, or EMPTY)
        # and create a tuple of every where an EMPTY space is
        j = 0 # reset j (i.e. cell is zero during every new row)
        for cell in row:
            if cell == None: # found a potential move
                possibleMove = (i, j)
                # print("possible Move", possibleMove)
                setOfMoves.add(possibleMove)
            j += 1
        i += 1
    return setOfMoves
    # print(setOfMoves)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise exception if action is invalid (i.e., action is not in set of possible actions
    # for the given game board)
    if action not in actions(board):
        raise Exception("invalid move")

    # make a copy of the original board
    new_board = copy.deepcopy(board)

    # update new board based on action provided and whose turn it is
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
