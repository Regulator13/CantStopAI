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

#------------------------------------------------------#

#-------------------------Main----------------------------#
for i in range(0,10):
    roll = rollDice();
    print(roll)
    pair1,pair2 = pairDice(roll)
    print(pair1,pair2)
    
endProgram = input("Press Enter to end the game")
while(endProgram == None):
    continue

#--------------------------------------------------------#
    
    