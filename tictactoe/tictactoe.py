"""
Tic Tac Toe Player
"""

import math

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
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


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
