#Can't Stop Artificial Intelligence
#Programmed by: Isaiah Frey
#Project begin: 8/30/2018

#This program will allow the user to play against a computer in
#the board game Can't Stop. The computer will accept the outcome of
#a player's turn and then play it's own turn, rolling the 4 dice, and
#deciding when to stop or returning that it has 'busted'.

#----------------Update Log------------------------#
# v1.0.0 - 8/30
#   Added rollDice funtion to roll 4 dice
# v1.1.0 - 9/1
#   Added board, player inputs, and computer turn layout
#---------------------------------------------------#

#----------------Libraries-----------------------#
#import a library to produce random integers
from random import randint

#-------------------------Initializations--------------------#

#Create the board
turn = 1
board = ([[0,0,0,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
          [0,0,0,0,0,-2,-2,-2,-2,-2,-2,-2,-2],
          [0,0,0,0,0,0,0,-2,-2,-2,-2,-2,-2],
          [0,0,0,0,0,0,0,0,0,-2,-2,-2,-2],
          [0,0,0,0,0,0,0,0,0,0,0,-2,-2],
          [0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,-2,-2],
          [0,0,0,0,0,0,0,0,0,-2,-2,-2,-2],
          [0,0,0,0,0,0,0,-2,-2,-2,-2,-2,-2],
          [0,0,0,0,0,-2,-2,-2,-2,-2,-2,-2,-2],
          [0,0,0,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]])

#---------------------Functions------------------------#

#Function to roll 4 six sided dice
def rollDice():
    roll = [0,0,0,0]
    for i in range (0,4):
        roll[i] = randint(1,6)
    return roll

#Function to pair up the four dice
def pairDice(roll):
    #pair all posibilities
    pair1 = roll[0] + roll[1]
    pair2 = roll[2] + roll[3]
    pair3 = roll[0] + roll[2]
    pair4 = roll[1] + roll[3]
    pair5 = roll[0] + roll[3]
    pair6 = roll[1] + roll[2]
    return pair1, pair2, pair3, pair4, pair5, pair6

#Function to print the board out
def printBoard(board):
    for col in range(0,11):
        for row in range(0,13):
            if board[col][row] >= 0:
                print(board[col][row], end='')
            else:
                print(" ", end='')
        print()

#Function to check where the topmost marker is in a column for the computer
def checkCol(col):
    for row in range(0,13):
        if board[col][row]%2 == 1:
            return row
    return 0

#Function to check if a column is still open or if a player has reached the top of it
def checkOpen(col):
    if col == 2 or col == 12:
        if board[col-2][2] != 0:
            return False
    if col == 3 or col == 11:
        if board[col-2][4] != 0:
            return False
    if col == 4 or col == 10:
        if board[col-2][6] != 0:
            return False
    if col == 5 or col == 9:
        if board[col-2][8] != 0:
            return False
    if col == 6 or col == 8:
        if board[col-2][10] != 0:
            return False
    if col == 7:
        if board[col-2][12] != 0:
            return False
    return True

#------------------------------------------------------#

#-------------------------Main----------------------------#

#Game beginning
print("Welcome to the Can't Stop AI")
while True:
    try:
        players = int(input("How many human players do you have? Input a number 1-3. "))
    except ValueError:
        print("Please choose a number!")
        continue
    if players < 1 or players > 3:
        print("Please choose a number between 1 and 3.")
        continue
    else:
        break

#Take the players' turns first    
while turn > 0:
    print("Player %d's turn." %turn)
    #input marker 1
    while True:
        while True:
            try:
                mark1y = int(input("Enter which number your first marker was on or 0 for bust. "))
            except ValueError:
                print("Please choose a number!")
                continue
            if mark1y < 0 or mark1y > 12 or mark1y == 1:
                print("Please choose a number between 2 and 12 or 0 for bust.")
                continue
            else:
                break
        try:
            mark1x = int(input("Enter how high first value marker ended or 0 for bust. "))
        except ValueError:
            print("Please choose a number!")
            continue
        if mark1x == 0:
            break
        if mark1x >= 0 and mark1x <= 13:
            if board[mark1y-2][mark1x-1] >= 0:
                for row in range (0,12):
                    if turn == 3:
                        if board[mark1y-2][row] >= 8:
                            board[mark1y-2][row] -= 8
                    if turn == 2:
                        if board[mark1y-2][row] >= 12:
                            board[mark1y-2][row] -= 4
                        if board[mark1y-2][row] >= 4 and board[row][mark1y-2] < 8:
                            board[mark1y-2][row] -= 4
                    if turn == 1:
                        if board[mark1y-2][row] >= 14:
                            board[mark1y-2][row] -= 2
                        if board[mark1y-2][row] >= 10 and board[row][mark1y-2] < 12:
                            board[mark1y-2][row] -= 2
                        if board[mark1y-2][row] >= 6 and board[row][mark1y-2] < 8:
                            board[mark1y-2][row] -= 2
                        if board[mark1y-2][row] >= 2 and board[row][mark1y-2] < 4:
                            board[mark1y-2][row] -= 2
                board[mark1y-2][mark1x-1] += 2**(turn)
                break
            else:
                print("Please choose space on the board.")
                continue
            
    #Input marker 2
    while True:
        while True:
            try:
                mark2y = int(input("Enter which number your second marker was on or 0 for bust. "))
            except ValueError:
                print("Please choose a number!")
                continue
            if mark2y < 0 or mark2y > 12 or mark2y == 1:
                print("Please choose a number between 2 and 12 or 0 for bust.")
                continue
            else:
                break
        try:
            mark2x = int(input("Enter how high second value marker ended or 0 for bust. "))
        except ValueError:
            print("Please choose a number!")
            continue
        if mark2x == 0:
            break
        if mark2x >= 0 and mark2x <= 13:
            if board[mark2y-2][mark2x-1] >= 0:
                for row in range (0,12):
                    if turn == 3:
                        if board[mark2y-2][row] >= 8:
                            board[mark2y-2][row] -= 8
                    if turn == 2:
                        if board[mark2y-2][row] >= 12:
                            board[mark2y-2][row] -= 4
                        if board[mark2y-2][row] >= 4 and board[row][mark2y-2] < 8:
                            board[mark2y-2][row] -= 4
                    if turn == 1:
                        if board[mark2y-2][row] >= 14:
                            board[mark2y-2][row] -= 2
                        if board[mark2y-2][row] >= 10 and board[row][mark2y-2] < 12:
                            board[mark2y-2][row] -= 2
                        if board[mark2y-2][row] >= 6 and board[row][mark2y-2] < 8:
                            board[mark2y-2][row] -= 2
                        if board[mark2y-2][row] >= 2 and board[row][mark2y-2] < 4:
                            board[mark2y-2][row] -= 2
                board[mark2y-2][mark2x-1] += 2**(turn)
                break
            else:
                print("Please choose space on the board.")
                continue
            
    #Input marker 3
    while True:
        while True:
            try:
                mark3y = int(input("Enter which number your third marker was on or 0 for bust. "))
            except ValueError:
                print("Please choose a number!")
                continue
            if mark3y < 0 or mark2y > 12 or mark2y == 1:
                print("Please choose a number between 2 and 12 or 0 for bust.")
                continue
            else:
                break
        try:
            mark3x = int(input("Enter how high third value marker ended or 0 for bust. "))
        except ValueError:
            print("Please choose a number!")
            continue
        if mark3x == 0:
            break
        if mark3x >= 0 and mark3x <= 13:
            if board[mark3y-2][mark3x-1] >= 0:
                for row in range (0,12):
                    if turn == 3:
                        if board[mark3y-2][row] >= 8:
                            board[mark3y-2][row] -= 8
                    if turn == 2:
                        if board[mark3y-2][row] >= 12:
                            board[mark3y-2][row] -= 4
                        if board[mark3y-2][row] >= 4 and board[row][mark3y-2] < 8:
                            board[mark3y-2][row] -= 4
                    if turn == 1:
                        if board[mark3y-2][row] >= 14:
                            board[mark3y-2][row] -= 2
                        if board[mark3y-2][row] >= 10 and board[row][mark3y-2] < 12:
                            board[mark3y-2][row] -= 2
                        if board[mark3y-2][row] >= 6 and board[row][mark3y-2] < 8:
                            board[mark3y-2][row] -= 2
                        if board[mark3y-2][row] >= 2 and board[row][mark3y-2] < 4:
                            board[mark3y-2][row] -= 2
                board[mark3y-2][mark3x-1] += 2**(turn)
                break
            else:
                print("Please choose space on the board.")
                continue
            
    #Print the board
    printBoard(board)
    
    #Increment the turn
    if turn < players:
         turn += 1
    else:
         turn = 0

#Computer Player's turn
while turn == 0:
    print("Computer Player's turn")
    #Initalize the markers and pairs
    mark1 = [-1,-1]
    mark2 = [-1,-1]
    mark3 = [-1,-1]
    pair1 = 0
    pair2 = 0
    #Roll the dice
    roll = rollDice()
    #Pair the dice into two pairs
    pair1, pair2, pair3, pair4, pair5, pair6 = pairDice(roll)
    #Check if there is already a marker on either of those pairs
    if pair1 == 0 and pair2 == 0:
        break
    mark1 = [pair1-2,checkCol(pair1-2)]
    mark2 = [pair2-2,checkCol(pair2-2)]
    #Finalize the output
    if mark1 != [-1,-1]:
        board[mark1[0]][mark1[1]] += 1
    if mark2 != [-1,-1]:
        board[mark2[0]][mark2[1]] += 1
    if mark3 != [-1,-1]:
        board[mark3[0]][mark3[1]] += 1
    printBoard(board)
    turn = 1
    
endProgram = input("Press Enter to end the game")
while(endProgram == None):
    continue

#--------------------------------------------------------#

