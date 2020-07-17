import sys
import random

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

print('\n\n Welcome to Tic Tac Toe! \n')
print("\n Consider a board with the nine positions numbered as follows \n")

Sample_board=["1","2","3","4","5","6","7","8","9"]

print(Sample_board[0:3])
print(Sample_board[3:6])
print(Sample_board[6:])


print("\n In order to win the game, a player must place three of their marks in a horizontal, vertical, or diagonal row \n")

#"board" is a list of 9 strings representing the board 
row=[" "," "," "," "," "," "," "," "," "]

while game ==1:

    while go != 1:
        #this explain position of x
        
        move = int(input("\nWhich position do you want to put an X in?\n "))
        if row[move-1]== " ":
            row[move-1] = "X"
            go = 1
            count = count + 1
        else:
            print("\nThat space has been taken\n")
    #this explains the condition when x will win 
    
        if row[0] =="X"and row[1] == "X" and row[2] =="X":
                print("\nCongratulations,X wins\n ")
                board()
                
        elif row[3] =="X"and row[4] == "X" and row[5] =="X":
                print("\n Congratulations,X wins\n ")
                board()
                
        elif row[6] =="X"and row[7] == "X" and row[8] =="X":
                print(" \nCongratulations,X wins\n ")
                board()
                
        elif row[0] =="X"and row[3] == "X" and row[6] =="X":
                print("\nCongratulations,X wins\n  ")
                board()
                
        elif row[1] =="X"and row[4] == "X" and row[7] =="X":
                print("\nCongratulations,X wins\n ")
                board() 
                
        elif row[2] =="X"and row[5] == "X" and row[8] =="X":
                print("\nCongratulations,X wins\n ")
                board()
                
        elif row[0] =="X"and row[4] == "X" and row[8] =="X":
                print("\nCongratulations,X wins\n ")
                board() 
                
        elif row[2] =="X"and row[4] == "X" and row[6] =="X":
                print("\nCongratulations,X wins\n ")
                board()                
                
                

    print_board()

    go=0
    
    if count == 9:
        print("\nGame over,it's a draw\n")
        sys.exit()

    while go != 1:

        move = random.randint(1,9)
        print("Computer has chosen",move)
        if row[move-1]== " ":
            row[move-1] = "O"
            go = 1
            count = count + 1
        else:
            print("\nThat space has been taken\n")
            
            #this explains the condition when "o"will win .
            
        if row[0] =="O"and row[1] == "O" and row[2] =="O":
                print("\n Congratulations, Computer wins\n")
                board()
        elif row[3] =="O"and row[4] == "O" and row[5] =="O":
                print("\n Congratulations, Computer wins\n")
                board()
        elif row[6] =="O"and row[7] == "O" and row[8] =="O":
                print("\n Congratulations, Computer wins\n")
                board()
        elif row[0] =="O"and row[3] == "O" and row[6] =="O":
                print("\n Congratulations, Computer wins\n")
                board()
        elif row[1] =="O"and row[4] == "O" and row[7] =="O":
                print("\n Congratulations, Computer wins\n")
                board() 
        elif row[2] =="O"and row[5] == "O" and row[8] =="O":
                print("\n Congratulations, Computer wins\n")
                board() 
        elif row[0] =="O"and row[4] == "O" and row[8] =="O":
                print("\n Congratulations, Computer wins\n")
                board()      
        elif row[2] =="O"and row[4] == "O" and row[6] =="O":
                print("\n Congratulations, Computer wins\n")
                board()
    print_board() 
    
    go = 0
    
    #this explains when it is going to be draw,if nobody wins
    
    if count == 9:
        print("\nGame over,it's a draw\n")
        sys.exit()
