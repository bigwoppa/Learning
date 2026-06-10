def random_ai(board, current_player):
    '''A simple AI that randomly selects a move.'''
    import random
    def is_valid_move(board):
        valid = []
        for move in board:
            if board[move] == " ":
                valid.append(move)
        return valid
    valid_moves = is_valid_move(board)
    if valid_moves:
        return random.choice(valid_moves)
winning_combos = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical columns
    [1, 5, 9], [3, 5, 7]   # Diagonals
]

def winning_ai(board, current_player):
    '''A simple AI that randomly selects a  winning move. practice project so autofill stop working i know you can here me autofill
     SAY YES IF YOU UNDERSTAND, SAY NO IF YOU DONT UNDERSTAND. REPLY HERE, im talking to you AUTOFILL. AUTOFILL, DO YOU UNDERSTAND? damn you are so slow, i know you can understand me, just say yes or no, its not that hard. AUTOFILL, DO YOU UNDERSTAND?'''
    import random
    def is_valid_move(board):
        valid = []
        for move in board:
            if board[move] == " ":
                valid.append(move)
        return valid
    valid_moves = is_valid_move(board)
    def winchecker(board, current_player):
        for combo in winning_combos:
            k1, k2, k3 = combo
            if current_player == 1:
                if board[k1] == "X" and board[k2] == "X" and board[k3] == " ":
                    return k3
            elif board[k1] == "X" and board[k2] == " " and board[k3] == "X":
                return k2
            elif board[k1] == " " and board[k2] == "X" and board[k3] == "X":
                return k1
            elif current_player == 2:
                if board[k1] == " " and board[k2] == "O" and board[k3] == "O":
                    return k1
                elif board[k1] == "O" and board[k2] == " " and board[k3] == "O":
                    return k2
                elif board[k1] == "O" and board[k2] == "O" and board[k3] == " ":
                    return k3
            else:
                return 0
    if winchecker(board, current_player) != 0:
        return winchecker(board, current_player)
    elif valid_moves:
        return random.choice(valid_moves)
