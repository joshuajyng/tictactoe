#global variables
game_ongoing = True
winner = None
curr_player = "X"

#create tic tac toe board
board =["1","2","3",
        "4","5","6",
        "7","8","9",]

def show_board():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

def handle_turn(curr_player):
    #get position to place x or o
    position = int(input("Choose position from 1-9: ")) - 1
    while(board[position] == "X" or board[position] == "O"):
        position = int(input("Choose another position from 1-9: ")) - 1
    board[position] = curr_player
    show_board()
    flip_player()

def check_game_state():
    check_win()
    check_tie()

def check_win():
    global game_ongoing
    global winner
    #check rows
    row1 = board[0] == board[1] == board [2]
    row2 = board[3] == board[4] == board [5]
    row3 = board[6] == board[7] == board [8]
    rows = row1 or row2 or row3
    if (row1):
        winner = board[0]
    elif(row2):
        winner = board[3]
    elif(row3):
        winner = board[6]
    #check cols
    col1 =  board[0] == board[3] == board [6]
    col2 =  board[1] == board[4] == board [7]
    col3 =  board[2] == board[5] == board [8]
    cols = col1 or col2 or col3
    if (col1):
        winner = board[0]
    elif(col2):
        winner = board[1]
    elif(col3):
        winner = board[2]
    #check diagonal
    diag1 = board[0] == board[4] == board[8]
    diag2 = board[2] == board[4] == board[6]
    diags = diag1 or diag2
    if (diags):
        winner = board[4]

    if (rows or diags or cols):
        game_ongoing= False
      
    return

def check_tie():
    # if board full and no win
    global game_ongoing
    count = 0
    for i in board:
        if i == "X" or i == "O":
            count+= 1
    if (count == 9):
        game_ongoing = False
    return

def flip_player():
    #change input between X and O
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    else:
        curr_player = "X"

    return 

def play():
    #main game logic
    show_board()
    while game_ongoing:
        handle_turn(curr_player)
        check_game_state()
    if winner == "X" or winner =="O":
        print(winner + " won the game.")
    else:
        print("Tie")
    

if __name__ == "__main__":
    play()
