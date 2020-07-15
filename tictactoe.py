import sys

# This function prints out the board that it was passed
def board():
    print_board()
    sys.exit()
    
def print_board():
    print(row[0:3])
    print(row[3:6])
    print(row[6:])
    
go=0
game=1
count=0

print('Welcome to Tic Tac Toe!')
print("Consider a board with the nine positions numbered as follows")

Sample_board=["1","2","3","4","5","6","7","8","9"]

print(Sample_board[0:3])
print(Sample_board[3:6])
print(Sample_board[6:]) 

print("In order to win the game, a player must place three of their marks in a horizontal, vertical, or diagonal row")

#"board" is a list of 9 strings representing the board 
row=[" "," "," "," "," "," "," "," "," "]

while game ==1:

    while go != 1:
        #this explain position of x
        
        move = int(input("which position do you want to put x in?"))
        if row[move-1]== " ":
            row[move-1] = "x"
            go = 1
            count = count + 1
        else:
            print("That space has been taken")
    #this explains the condition when x will win 
    
        if row[0] =="x"and row[1] == "x" and row[2] =="x":
                print("X wins")
                board()
        elif row[3] =="x"and row[4] == "x" and row[5] =="x":
                print("X wins")
                board()
        elif row[6] =="x"and row[7] == "x" and row[8] =="x":
                print("X wins")
                board()
        elif row[0] =="x"and row[3] == "x" and row[6] =="x":
                print("X wins")
                board()
        elif row[1] =="x"and row[4] == "x" and row[7] =="x":
                print("X wins")
                board() 
        elif row[2] =="x"and row[5] == "x" and row[8] =="x":
                print("X wins")
                board() 
        elif row[0] =="x"and row[4] == "x" and row[8] =="x":
                print("X wins")
                board()       
        elif row[2] =="x"and row[4] == "x" and row[6] =="x":
                print("X wins")
                board()                
                
                

    print_board()

    go=0
    
    if count == 9:
        print("Game over,it's a draw")
        sys.exit()

    while go != 1:

        move = int(input("which position do you want to put o in?"))
        if row[move-1]== " ":
            row[move-1] = "o"
            go = 1
            count = count + 1
        else:
            print("That space has been taken")
            
            #this explains the condition when "o"will win .
            
        if row[0] =="o"and row[1] == "o" and row[2] =="o":
                print("O wins")
                board()
        elif row[3] =="o"and row[4] == "o" and row[5] =="o":
                print("O wins")
                board()
        elif row[6] =="o"and row[7] == "o" and row[8] =="o":
                print("O wins")
                board()
        elif row[0] =="o"and row[3] == "o" and row[6] =="o":
                print("O wins")
                board()
        elif row[1] =="o"and row[4] == "o" and row[7] =="o":
                print("O wins")
                board() 
        elif row[2] =="o"and row[5] == "o" and row[8] =="o":
                print("O wins")
                board() 
        elif row[0] =="o"and row[4] == "o" and row[8] =="o":
                print("O wins")
                board()      
        elif row[2] =="o"and row[4] == "o" and row[6] =="o":
                print("O wins")
                board()
    print_board() 
    
    go = 0
    
    #this explains when it is going to be draw,if nobody wins
    
    if count == 9:
        print("Game over,it's a draw")
        sys.exit()
