#ttt game code
board = [[0, 0, 0], 
        [1, 1, 0], 
        [0, 2, 0]]
def render(board_values): 
    print("+","-"*3,"+", sep="")
    for x in board_values:
        char = ""
        for v in x:
            if v == 0:
                char += "_"
            elif v == 1:
                char += "X"
            elif v == 2:
                char += "O"
            else:
                print("error foound")
        print("|",char,"|")
    print("+","-"*3,"+", sep="")
def get_move():
    pos = [[1, 2, 3], 
            [4, 5, 6], 
             [7, 8, 9]]
    select = input("Which tile have you decided upon")
    return(select)
def make_move(board, cords, current_player):

#loop through turns till game is over
while True:
    
    # TODO: not sure how ill do this yet

    current_player = ???
    
    render(board)

    cords = get_move()
    make_move(board, cords, current_player)


    winner = getwinner()

    if winner != None:
        print("Winner IS!!!!", winner)
        break

    if is_board_full(board):
        print("ITS A TIE")
        break
#repeat until GG