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
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_X = sum(row.count(X) for row in board)
    number_of_O = sum(row.count(O) for row in board)
    
    return X if number_of_X == number_of_O else O
    
        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid action: space occupied")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] is not None:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] is not None:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == 0:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action (i, j) for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    # X is the maximizing player
    if current_player == X:
        best_val = -float('inf')
        best_move = None
        for action in actions(board):
            # X checks what is the lowest value O can force after this move
            move_val = min_value(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_move = action
        return best_move

    # O is the minimizing player
    else:
        best_val = float('inf')
        best_move = None
        for action in actions(board):
            # O checks what is the highest value X can force after this move
            move_val = max_value(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_move = action
        return best_move

def max_value(board):
    """
    Helper function to find the maximum possible utility value.
    """
    if terminal(board):
        return utility(board)
    
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Helper function to find the minimum possible utility value.
    """
    if terminal(board):
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v