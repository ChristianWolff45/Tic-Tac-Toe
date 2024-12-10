import random, copy

#selects random move
def easy_bot_moves(board):
    empty_cells = [
            (row_index, col_index)
            for row_index, row in enumerate(board)
            for col_index, cell in enumerate(row)
            if cell == ""
        ]
    return random.choice(empty_cells)

#uses a broken algorithm to simulate the computer making a mistake
def medium_bot_moves(board):
    v= float('inf')
    bestAction = None
    for action in actions(board):
        temp = min_value(result(board, action))
        if temp < v:
            v = temp
            bestAction = action
    
    return bestAction


#finds the optimal bot move given an optimal playing opponent

def hard_bot_moves(board):
    v= float('inf')
    bestAction = None
    for action in actions(board):
        temp = max_value(result(board, action))
        if temp < v:
            v = temp
            bestAction = action
    return bestAction

# accepts the result of a board and an action 
# if the state is a terminal state, ie win, loss or tie returns the utility
# if the state is not a terminal state finds the optimal move by finding the move with the lowest util
def min_value(board):
    if(terminal(board)):
        return utility(board)
    v= float('inf')
    for action in actions(board):
       v = min(v, max_value(result(board, action)))
    return v

# accepts the result of a board and an action 
# if the state is a terminal state, ie win, loss or tie returns the utility
# if the state is not a terminal state finds the optimal move by finding the move with the highest util
def max_value(board):
    if(terminal(board)):
        return utility(board)
    v= float('-inf')
    for action in actions(board):
       v = max(v, min_value(result(board, action)))
    return v


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(board[1][1]!=""):
        player = board[1][1]
        if(board[0][0]==player and board[2][2]==player):
            return player
        if(board[0][1]==player and board[2][1]==player):
            return player
        if(board[0][2]==player and board[2][0]==player):
            return player
        if(board[1][0]==player and board[1][2]==player):
            return player
    if(board[0][0]!=""):
        player=board[0][0]
        if(board[0][1]==player and board[0][2]==player):
            return player
        if(board[1][0]==player and board[2][0]==player):
            return player
    if(board[2][2]!=""):
        player=board[2][2]
        if(board[1][2]==player and board[0][2]==player):
            return player
        if(board[2][1]==player and board[2][0]==player):
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True
    elif(all(cell != "" for row in board for cell in row)):
        return True    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board)=="O"):
        return -1
    if(winner(board)=="X"):
        return 1
    return 0
            
    
#finds all possible actions for the player
def actions(board):
    empty_cells = {
            (row_index, col_index)
            for row_index, row in enumerate(board)
            for col_index, cell in enumerate(row)
            if cell == ""
    }
    return empty_cells

#returns a new board after adding a move to the board
def result(board, action):
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = get_player(board)
    return new_board

#determines the player of the game by counting the the Xs and Os on the board
#if More Xs than Os it is Os turn
def get_player(board):
    X = 0
    O = 0
    for row in board:
        for cell in row:
            if cell == "X":
                X = X +1
            if cell == "O":
                O = O + 1
    if X > O:
        return "O"
    else:
        return "X"
    




