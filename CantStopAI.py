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
#---------------------------------------------------#

#----------------Libraries-----------------------#
#import a library to produce random integers
from random import randint

#-------------------------Initializations--------------------#

#Create the board
turn = 1
board = ([[0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [-1,0,0,0,0,0,0,0,0,0,-1],
          [-1,0,0,0,0,0,0,0,0,0,-1],
          [-1,-1,0,0,0,0,0,0,0,-1,-1],
          [-1,-1,0,0,0,0,0,0,0,-1,-1],
          [-1,-1,-1,0,0,0,0,0,-1,-1,-1],
          [-1,-1,-1,0,0,0,0,0,-1,-1,-1],
          [-1,-1,-1,-1,0,0,0,-1,-1,-1,-1],
          [-1,-1,-1,-1,0,0,0,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1]])
#---------------------Functions------------------------#

#Function to roll 4 six sided dice
def rollDice():
    roll = [0,0,0,0]
    for i in range (0,4):
        roll[i] = randint(1,6)
    return roll

def pairDice(roll):
    pair1 = roll[0] + roll[1]
    pair2 = roll[2] + roll[3]
    return pair1, pair2

def printBoard(board):
    for row in range(0,13):
        for col in range(0,11):
            if board[12-row][col] >= 0:
                print(board[12-row][col], end='')
            else:
                print(" ", end='')
        print()

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
            if board[mark1x-1][mark1y-2] >= 0:
                for row in range (0,12):
                    if turn == 3:
                        if board[row][mark1y-2] >= 8:
                            board[row][mark1y-2] -= 8
                    if turn == 2:
                        if board[row][mark1y-2] >= 12:
                            board[row][mark1y-2] -= 4
                        if board[row][mark1y-2] >= 4 and board[row][mark1y-2] < 8:
                            board[row][mark1y-2] -= 4
                    if turn == 1:
                        if board[row][mark1y-2] >= 14:
                            board[row][mark1y-2] -= 2
                        if board[row][mark1y-2] >= 10 and board[row][mark1y-2] < 12:
                            board[row][mark1y-2] -= 2
                        if board[row][mark1y-2] >= 6 and board[row][mark1y-2] < 8:
                            board[row][mark1y-2] -= 2
                        if board[row][mark1y-2] >= 2 and board[row][mark1y-2] < 4:
                            board[row][mark1y-2] -= 2
                board[mark1x-1][mark1y-2] += 2**(turn)
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
            if board[mark2x-1][mark2y-2] >= 0:
                for row in range (0,12):
                    if turn == 3:
                        if board[row][mark2y-2] >= 8:
                            board[row][mark2y-2] -= 8
                    if turn == 2:
                        if board[row][mark2y-2] >= 12:
                            board[row][mark2y-2] -= 4
                        if board[row][mark2y-2] >= 4 and board[row][mark2y-2] < 8:
                            board[row][mark2y-2] -= 4
                    if turn == 1:
                        if board[row][mark2y-2] >= 14:
                            board[row][mark2y-2] -= 2
                        if board[row][mark2y-2] >= 10 and board[row][mark2y-2] < 12:
                            board[row][mark2y-2] -= 2
                        if board[row][mark2y-2] >= 6 and board[row][mark2y-2] < 8:
                            board[row][mark2y-2] -= 2
                        if board[row][mark2y-2] >= 2 and board[row][mark2y-2] < 4:
                            board[row][mark2y-2] -= 2
                board[mark2x-1][mark2y-2] += 2**(turn)
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
            if board[mark3x-1][mark3y-2] >= 0:
                for row in range (0,12):
                    if turn == 3:
                        if board[row][mark3y-2] >= 8:
                            board[row][mark3y-2] -= 8
                    if turn == 2:
                        if board[row][mark3y-2] >= 12:
                            board[row][mark3y-2] -= 4
                        if board[row][mark3y-2] >= 4 and board[row][mark3y-2] < 8:
                            board[row][mark3y-2] -= 4
                    if turn == 1:
                        if board[row][mark3y-2] >= 14:
                            board[row][mark3y-2] -= 2
                        if board[row][mark3y-2] >= 10 and board[row][mark3y-2] < 12:
                            board[row][mark3y-2] -= 2
                        if board[row][mark3y-2] >= 6 and board[row][mark3y-2] < 8:
                            board[row][mark3y-2] -= 2
                        if board[row][mark3y-2] >= 2 and board[row][mark3y-2] < 4:
                            board[row][mark3y-2] -= 2
                board[mark3x-1][mark3y-2] += 2**(turn)
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
         turn = 1

endProgram = input("Press Enter to end the game")
while(endProgram == None):
    continue

#--------------------------------------------------------#
    
    