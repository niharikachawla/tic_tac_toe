import random

command = 'r'

# This function prints out the board that it was passed
def print_board():
    print(row[0:3])
    print(row[3:6])
    print(row[6:])

def board():
    print_board()
    
def game_win():
    var = 0
    if (row[0] == row[1] == row[2] and row[0] != ' '):
        if row[0] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
        
    if (row[3] == row[4] == row[5] and row[3] != ' '):
        if row[3] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
        
    if (row[6] == row[7] == row[8] and row[6] != ' '):
        if row[6] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
        
    if (row[0] == row[3] == row[6] and row[0] != ' '):
        if row[0] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
                
    if (row[1] == row[4] == row[7] and row[1] != ' '):
        if row[1] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board() 
                
    if (row[2] == row[5] == row[8] and row[2] != ' '):
        if row[2] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
                
    if (row[0] == row[4] == row[8] and row[0] != ' '):
        if row[0] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
                
    if (row[2] == row[4] == row[6] and row[2] != ' '):
        if row[2] == 'X':
            print("\nCongratulations,X wins\n ")
        else:
            print("\nCongratulations, Computer wins\n ")
        var = 1
        board()
        
    if count ==9:
        print("\nGame over,it's a draw\n")
        var = 1
        board()
    return var                

while True:
    if command == 'e':
        print("Exiting Game")
        break
    
    row=[" "," "," "," "," "," "," "," "," "]
    count=0
    print('\n\n Welcome to Tic Tac Toe! \n')
    print("\n Consider a board with the nine positions numbered as follows \n")
    Sample_board=["1","2","3","4","5","6","7","8","9"]

    print(Sample_board[0:3])
    print(Sample_board[3:6])
    print(Sample_board[6:])
    print("\n In order to win the game, a player must place three of their marks in a horizontal, vertical, or diagonal row \n")
    go = 0
    
    while go == 0:
        #"board" is a list of 9 strings representing the board 
        
        move = int(input("\nWhich position do you want to put an X in?\n "))
        while row[move-1] != " ":
            print("\nThat space has been taken\n")
            move = int(input("\nChoose another value of X\n "))
        
        row[move-1] = 'X'
        count = count + 1
        
        print_board()
        
        if count >=5:
            go = game_win()
            if go == 1:
                command = input('Enter r to restart, or e to end game: ')
                break
        
        move = random.randint(1,9)
        print("Computer has chosen",move)
        
        while row[move-1] != " ":
            move = random.randint(1,9)
        
        row[move-1] = 'O'
        count = count + 1
        
        print_board()
        
        if count >=5:
            go = game_win()
            if go == 1:
                command = input('Enter r to restart, or e to end game: ')

