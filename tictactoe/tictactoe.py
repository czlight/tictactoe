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
    i = 0  # row
    j = 0  # cell
    setOfMoves = set()
    # iterate over every row (i.e., list) of the game board
    for row in board:
        # iterate over every item in row (i.e., X, O, or EMPTY)
        # and create a tuple of every where an EMPTY space is
        j = 0  # reset j (i.e. cell is zero during every new row)
        for cell in row:
            if cell == None:  # found a potential move
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


def equal(list):
    # transform the row into a set; if it's length is 1, all elements were the same
    if len(set(list)) == 1 and list[0] != None:
        return True


def determine_value(list):
    if list[0] == X:
        return X
    else:
        return O


def winner(board):
    """
    Returns the winner of the game, or None if there's no winner (i.e., tie game
    or game is in progress)
    """
    # determine if there's a horizontal winner
    for row in board:
        if equal(row):
            return determine_value(row)

    # create a list for each column
    columns = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

    # create list for for potential diagonal winner (i.e., 0,0; 1,1; 2,2)
    diagonal1 = []
    diagonal2 = []
    for i in range(3):
        diagonal1.append(board[i][i])

    for i in range(3):
        diagonal2.append(board[i][2 - i])

    # check if there's a diagonal winner
    if equal(diagonal1):
        return determine_value(diagonal1)

    if equal(diagonal2):
        return determine_value(diagonal2)

    # check if each element in column is the same
    for column in columns:
        if equal(column):
            return determine_value(column)

    # no winner (i.e., game in progress or tie)
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # there's a winner if X or O wins or if the actions() indicates there are no possible moves
    if winner(board) == X or winner(board) == O or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1

    if winner(board) == None:
        return 0


def find_max_value(board):
    """
    returns action that gives the optimal move (i.e. max value)
    and utility in a given state
    """
    print("calling find_max_value......!")
    # if we're in a terminal state, return the utility of the board
    if terminal(board) == True:
        return utility(board), None

    # keep track of value of state, initialize to negative infinity
    # I'm always going to try and do better than that
    max_value = float("-inf")
    max_action = None

    # go through all possible actions and find out the max score, given what my opponent is trying to do
    for action in actions(board):
        min_value, min_action = find_min_value(result(board, action))

        if min_value > max_value:
            max_value = min_value
            max_action = action

    return max_value, max_action


def find_min_value(board):
    """
    returns the optimal action (i.e., minimum value)
    and utility for a given state

    """

    if terminal(board) == True:
        return utility(board), None

    min_value = float("inf")
    min_action = None

    # go through all available actions and determine the min score, given what opponent is trying to do
    for action in actions(board):

        max_value, max_action = find_max_value(result(board, action))

        print("value (from find_max_value):", max_value)
        if max_value < min_value:
            min_value = max_value
            min_action = action

    return min_value, min_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # return None if board is in a Terminal state
    if terminal(board) == True:
        return None

    current_player = player(board)

    if current_player == "X":
        value, action = find_max_value(board)

    if current_player == "O":
        value, action = find_min_value(board)

    return action
