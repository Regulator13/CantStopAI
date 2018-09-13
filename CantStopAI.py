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
import copy
#-------------------------Initializations--------------------#

#Probability array initializations
prob1 = [0.132, 0.233, 0.356, 0.447, 0.561, 0.644, 0.561, 0.447, 0.356, 0.233, 0.132]

prob2 = [[0.132, 0.32, 0.439, 0.526, 0.633, 0.713, 0.669, 0.561, 0.474, 0.356, 0.26],
         [0.32, 0.232, 0.47, 0.532, 0.635, 0.71, 0.682, 0.643, 0.561, 0.447, 0.355],
         [0.439, 0.47, 0.356, 0.61, 0.72, 0.77, 0.746, 0.683, 0.67, 0.561, 0.474],
         [0.526, 0.532, 0.61, 0.447, 0.732, 0.776, 0.768, 0.692, 0.683, 0.644, 0.561],
         [0.633, 0.635, 0.72, 0.732, 0.56, 0.835, 0.823, 0.769, 0.747, 0.682, 0.669],
         [0.713, 0.71, 0.77, 0.776, 0.835, 0.644, 0.835, 0.777, 0.77, 0.711, 0.713],
         [0.669, 0.682, 0.746, 0.768, 0.823, 0.835, 0.56, 0.732, 0.72, 0.636, 0.634],
         [0.561, 0.643, 0.683, 0.692, 0.769, 0.777, 0.732, 0.448, 0.61, 0.533, 0.526],
         [0.474, 0.561, 0.67, 0.683, 0.747, 0.77, 0.72, 0.61, 0.356, 0.47, 0.438],
         [0.356, 0.447, 0.561, 0.644, 0.682, 0.711, 0.636, 0.533, 0.47, 0.233, 0.321],
         [0.26, 0.355, 0.474, 0.561, 0.669, 0.713, 0.634, 0.526, 0.438, 0.321, 0.132]]

prob3 = [[[0.132, 0.321, 0.44, 0.527, 0.634, 0.713, 0.669, 0.561, 0.473, 0.355, 0.26], [0.321, 0.321, 0.523, 0.586, 0.683, 0.753, 0.756, 0.712, 0.634, 0.525, 0.439], [0.44, 0.523, 0.44, 0.659, 0.758, 0.807, 0.816, 0.756, 0.738, 0.635, 0.553], [0.527, 0.586, 0.659, 0.527, 0.771, 0.81, 0.828, 0.761, 0.757, 0.713, 0.636], [0.634, 0.683, 0.758, 0.771, 0.634, 0.864, 0.883, 0.833, 0.81, 0.755, 0.738], [0.713, 0.753, 0.807, 0.81, 0.864, 0.713, 0.891, 0.836, 0.833, 0.779, 0.781], [0.669, 0.756, 0.816, 0.828, 0.883, 0.891, 0.669, 0.822, 0.815, 0.735, 0.738], [0.561, 0.712, 0.756, 0.761, 0.833, 0.836, 0.822, 0.561, 0.709, 0.636, 0.634], [0.473, 0.634, 0.738, 0.757, 0.81, 0.833, 0.815, 0.709, 0.473, 0.578, 0.551], [0.355, 0.525, 0.635, 0.713, 0.755, 0.779, 0.735, 0.636, 0.578, 0.355, 0.438], [0.26, 0.439, 0.553, 0.636, 0.738, 0.781, 0.738, 0.634, 0.551, 0.438, 0.26]],
         [[0.321, 0.321, 0.523, 0.586, 0.683, 0.753, 0.756, 0.712, 0.634, 0.525, 0.439], [0.321, 0.234, 0.471, 0.534, 0.636, 0.71, 0.682, 0.643, 0.561, 0.447, 0.357], [0.523, 0.471, 0.471, 0.67, 0.742, 0.791, 0.797, 0.779, 0.756, 0.657, 0.58], [0.586, 0.534, 0.67, 0.534, 0.771, 0.788, 0.808, 0.777, 0.759, 0.71, 0.638], [0.683, 0.636, 0.742, 0.771, 0.636, 0.865, 0.853, 0.826, 0.822, 0.758, 0.736], [0.753, 0.71, 0.791, 0.788, 0.865, 0.71, 0.893, 0.843, 0.836, 0.777, 0.779], [0.756, 0.682, 0.797, 0.808, 0.853, 0.893, 0.682, 0.835, 0.833, 0.758, 0.756], [0.712, 0.643, 0.779, 0.777, 0.826, 0.843, 0.835, 0.643, 0.778, 0.71, 0.712], [0.634, 0.561, 0.756, 0.759, 0.822, 0.836, 0.833, 0.778, 0.561, 0.656, 0.634], [0.525, 0.447, 0.657, 0.71, 0.758, 0.777, 0.758, 0.71, 0.656, 0.447, 0.525], [0.439, 0.357, 0.58, 0.638, 0.736, 0.779, 0.756, 0.712, 0.634, 0.525, 0.357]],
         [[0.44, 0.523, 0.44, 0.659, 0.758, 0.807, 0.816, 0.756, 0.738, 0.635, 0.553], [0.523, 0.471, 0.471, 0.67, 0.742, 0.791, 0.797, 0.779, 0.756, 0.657, 0.58], [0.44, 0.471, 0.357, 0.612, 0.721, 0.769, 0.747, 0.683, 0.67, 0.561, 0.475], [0.659, 0.67, 0.612, 0.612, 0.797, 0.848, 0.846, 0.799, 0.823, 0.779, 0.711], [0.758, 0.742, 0.721, 0.797, 0.721, 0.886, 0.911, 0.864, 0.883, 0.833, 0.816], [0.807, 0.791, 0.769, 0.848, 0.886, 0.769, 0.903, 0.893, 0.877, 0.836, 0.833], [0.816, 0.797, 0.747, 0.846, 0.911, 0.903, 0.747, 0.863, 0.884, 0.823, 0.811], [0.756, 0.779, 0.683, 0.799, 0.864, 0.893, 0.863, 0.683, 0.822, 0.759, 0.756], [0.738, 0.756, 0.67, 0.823, 0.883, 0.877, 0.884, 0.822, 0.67, 0.756, 0.738], [0.635, 0.657, 0.561, 0.779, 0.833, 0.836, 0.823, 0.759, 0.756, 0.561, 0.635], [0.553, 0.58, 0.475, 0.711, 0.816, 0.833, 0.811, 0.756, 0.738, 0.635, 0.475]],
         [[0.527, 0.586, 0.659, 0.527, 0.771, 0.81, 0.828, 0.761, 0.757, 0.713, 0.636], [0.586, 0.534, 0.67, 0.534, 0.771, 0.788, 0.808, 0.777, 0.759, 0.71, 0.638], [0.659, 0.67, 0.612, 0.612, 0.797, 0.848, 0.846, 0.799, 0.823, 0.779, 0.711], [0.527, 0.534, 0.612, 0.449, 0.733, 0.777, 0.769, 0.692, 0.683, 0.644, 0.562], [0.771, 0.771, 0.797, 0.733, 0.733, 0.887, 0.895, 0.867, 0.863, 0.836, 0.823], [0.81, 0.788, 0.848, 0.777, 0.887, 0.777, 0.914, 0.854, 0.893, 0.843, 0.836], [0.828, 0.808, 0.846, 0.769, 0.895, 0.914, 0.769, 0.866, 0.864, 0.826, 0.833], [0.761, 0.777, 0.799, 0.692, 0.867, 0.854, 0.866, 0.692, 0.799, 0.777, 0.761], [0.757, 0.759, 0.823, 0.683, 0.863, 0.893, 0.864, 0.799, 0.683, 0.779, 0.756], [0.713, 0.71, 0.779, 0.644, 0.836, 0.843, 0.826, 0.777, 0.779, 0.644, 0.712], [0.636, 0.638, 0.711, 0.562, 0.823, 0.836, 0.833, 0.761, 0.756, 0.712, 0.562]],
         [[0.634, 0.683, 0.758, 0.771, 0.634, 0.864, 0.883, 0.833, 0.81, 0.755, 0.738], [0.683, 0.636, 0.742, 0.771, 0.636, 0.865, 0.853, 0.826, 0.822, 0.758, 0.736], [0.758, 0.742, 0.721, 0.797, 0.721, 0.886, 0.911, 0.864, 0.883, 0.833, 0.816], [0.771, 0.771, 0.797, 0.733, 0.733, 0.887, 0.895, 0.867, 0.863, 0.836, 0.823], [0.634, 0.636, 0.721, 0.733, 0.56, 0.835, 0.823, 0.769, 0.746, 0.682, 0.669], [0.864, 0.865, 0.886, 0.887, 0.835, 0.835, 0.92, 0.914, 0.903, 0.893, 0.89], [0.883, 0.853, 0.911, 0.895, 0.823, 0.92, 0.823, 0.895, 0.911, 0.852, 0.883], [0.833, 0.826, 0.864, 0.867, 0.769, 0.914, 0.895, 0.769, 0.845, 0.807, 0.828], [0.81, 0.822, 0.883, 0.863, 0.746, 0.903, 0.911, 0.845, 0.746, 0.795, 0.815], [0.755, 0.758, 0.833, 0.836, 0.682, 0.893, 0.852, 0.807, 0.795, 0.682, 0.755], [0.738, 0.736, 0.816, 0.823, 0.669, 0.89, 0.883, 0.828, 0.815, 0.755, 0.669]],
         [[0.713, 0.753, 0.807, 0.81, 0.864, 0.713, 0.891, 0.836, 0.833, 0.779, 0.781], [0.753, 0.71, 0.791, 0.788, 0.865, 0.71, 0.893, 0.843, 0.836, 0.777, 0.779], [0.807, 0.791, 0.769, 0.848, 0.886, 0.769, 0.903, 0.893, 0.877, 0.836, 0.833], [0.81, 0.788, 0.848, 0.777, 0.887, 0.777, 0.914, 0.854, 0.893, 0.843, 0.836], [0.864, 0.865, 0.886, 0.887, 0.835, 0.835, 0.92, 0.914, 0.903, 0.893, 0.89], [0.713, 0.71, 0.769, 0.777, 0.835, 0.644, 0.836, 0.776, 0.769, 0.71, 0.712], [0.891, 0.893, 0.903, 0.914, 0.92, 0.836, 0.836, 0.886, 0.886, 0.865, 0.864], [0.836, 0.843, 0.893, 0.854, 0.914, 0.776, 0.886, 0.776, 0.848, 0.787, 0.809], [0.833, 0.836, 0.877, 0.893, 0.903, 0.769, 0.886, 0.848, 0.769, 0.79, 0.807], [0.779, 0.777, 0.836, 0.843, 0.893, 0.71, 0.865, 0.787, 0.79, 0.71, 0.752], [0.781, 0.779, 0.833, 0.836, 0.89, 0.712, 0.864, 0.809, 0.807, 0.752, 0.712]],
         [[0.669, 0.756, 0.816, 0.828, 0.883, 0.891, 0.669, 0.822, 0.815, 0.735, 0.738], [0.756, 0.682, 0.797, 0.808, 0.853, 0.893, 0.682, 0.835, 0.833, 0.758, 0.756], [0.816, 0.797, 0.747, 0.846, 0.911, 0.903, 0.747, 0.863, 0.884, 0.823, 0.811], [0.828, 0.808, 0.846, 0.769, 0.895, 0.914, 0.769, 0.866, 0.864, 0.826, 0.833], [0.883, 0.853, 0.911, 0.895, 0.823, 0.92, 0.823, 0.895, 0.911, 0.852, 0.883], [0.891, 0.893, 0.903, 0.914, 0.92, 0.836, 0.836, 0.886, 0.886, 0.865, 0.864], [0.669, 0.682, 0.747, 0.769, 0.823, 0.836, 0.56, 0.731, 0.72, 0.635, 0.633], [0.822, 0.835, 0.863, 0.866, 0.895, 0.886, 0.731, 0.731, 0.795, 0.77, 0.769], [0.815, 0.833, 0.884, 0.864, 0.911, 0.886, 0.72, 0.795, 0.72, 0.742, 0.758], [0.735, 0.758, 0.823, 0.826, 0.852, 0.865, 0.635, 0.77, 0.742, 0.635, 0.682], [0.738, 0.756, 0.811, 0.833, 0.883, 0.864, 0.633, 0.769, 0.758, 0.682, 0.633]],
         [[0.561, 0.712, 0.756, 0.761, 0.833, 0.836, 0.822, 0.561, 0.709, 0.636, 0.634], [0.712, 0.643, 0.779, 0.777, 0.826, 0.843, 0.835, 0.643, 0.778, 0.71, 0.712], [0.756, 0.779, 0.683, 0.799, 0.864, 0.893, 0.863, 0.683, 0.822, 0.759, 0.756], [0.761, 0.777, 0.799, 0.692, 0.867, 0.854, 0.866, 0.692, 0.799, 0.777, 0.761], [0.833, 0.826, 0.864, 0.867, 0.769, 0.914, 0.895, 0.769, 0.845, 0.807, 0.828], [0.836, 0.843, 0.893, 0.854, 0.914, 0.776, 0.886, 0.776, 0.848, 0.787, 0.809], [0.822, 0.835, 0.863, 0.866, 0.895, 0.886, 0.731, 0.731, 0.795, 0.77, 0.769], [0.561, 0.643, 0.683, 0.692, 0.769, 0.776, 0.731, 0.447, 0.609, 0.532, 0.525], [0.709, 0.778, 0.822, 0.799, 0.845, 0.848, 0.795, 0.609, 0.609, 0.668, 0.656], [0.636, 0.71, 0.759, 0.777, 0.807, 0.787, 0.77, 0.532, 0.668, 0.532, 0.583], [0.634, 0.712, 0.756, 0.761, 0.828, 0.809, 0.769, 0.525, 0.656, 0.583, 0.525]],
         [[0.473, 0.634, 0.738, 0.757, 0.81, 0.833, 0.815, 0.709, 0.473, 0.578, 0.551], [0.634, 0.561, 0.756, 0.759, 0.822, 0.836, 0.833, 0.778, 0.561, 0.656, 0.634], [0.738, 0.756, 0.67, 0.823, 0.883, 0.877, 0.884, 0.822, 0.67, 0.756, 0.738], [0.757, 0.759, 0.823, 0.683, 0.863, 0.893, 0.864, 0.799, 0.683, 0.779, 0.756], [0.81, 0.822, 0.883, 0.863, 0.746, 0.903, 0.911, 0.845, 0.746, 0.795, 0.815], [0.833, 0.836, 0.877, 0.893, 0.903, 0.769, 0.886, 0.848, 0.769, 0.79, 0.807], [0.815, 0.833, 0.884, 0.864, 0.911, 0.886, 0.72, 0.795, 0.72, 0.742, 0.758], [0.709, 0.778, 0.822, 0.799, 0.845, 0.848, 0.795, 0.609, 0.609, 0.668, 0.656], [0.473, 0.561, 0.67, 0.683, 0.746, 0.769, 0.72, 0.609, 0.355, 0.469, 0.437], [0.578, 0.656, 0.756, 0.779, 0.795, 0.79, 0.742, 0.668, 0.469, 0.469, 0.52], [0.551, 0.634, 0.738, 0.756, 0.815, 0.807, 0.758, 0.656, 0.437, 0.52, 0.437]],
         [[0.355, 0.525, 0.635, 0.713, 0.755, 0.779, 0.735, 0.636, 0.578, 0.355, 0.438], [0.525, 0.447, 0.657, 0.71, 0.758, 0.777, 0.758, 0.71, 0.656, 0.447, 0.525], [0.635, 0.657, 0.561, 0.779, 0.833, 0.836, 0.823, 0.759, 0.756, 0.561, 0.635], [0.713, 0.71, 0.779, 0.644, 0.836, 0.843, 0.826, 0.777, 0.779, 0.644, 0.712], [0.755, 0.758, 0.833, 0.836, 0.682, 0.893, 0.852, 0.807, 0.795, 0.682, 0.755], [0.779, 0.777, 0.836, 0.843, 0.893, 0.71, 0.865, 0.787, 0.79, 0.71, 0.752], [0.735, 0.758, 0.823, 0.826, 0.852, 0.865, 0.635, 0.77, 0.742, 0.635, 0.682], [0.636, 0.71, 0.759, 0.777, 0.807, 0.787, 0.77, 0.532, 0.668, 0.532, 0.583], [0.578, 0.656, 0.756, 0.779, 0.795, 0.79, 0.742, 0.668, 0.469, 0.469, 0.52], [0.355, 0.447, 0.561, 0.644, 0.682, 0.71, 0.635, 0.532, 0.469, 0.232, 0.319], [0.438, 0.525, 0.635, 0.712, 0.755, 0.752, 0.682, 0.583, 0.52, 0.319, 0.319]],
         [[0.26, 0.439, 0.553, 0.636, 0.738, 0.781, 0.738, 0.634, 0.551, 0.438, 0.26], [0.439, 0.357, 0.58, 0.638, 0.736, 0.779, 0.756, 0.712, 0.634, 0.525, 0.357], [0.553, 0.58, 0.475, 0.711, 0.816, 0.833, 0.811, 0.756, 0.738, 0.635, 0.475], [0.636, 0.638, 0.711, 0.562, 0.823, 0.836, 0.833, 0.761, 0.756, 0.712, 0.562], [0.738, 0.736, 0.816, 0.823, 0.669, 0.89, 0.883, 0.828, 0.815, 0.755, 0.669], [0.781, 0.779, 0.833, 0.836, 0.89, 0.712, 0.864, 0.809, 0.807, 0.752, 0.712], [0.738, 0.756, 0.811, 0.833, 0.883, 0.864, 0.633, 0.769, 0.758, 0.682, 0.633], [0.634, 0.712, 0.756, 0.761, 0.828, 0.809, 0.769, 0.525, 0.656, 0.583, 0.525], [0.551, 0.634, 0.738, 0.756, 0.815, 0.807, 0.758, 0.656, 0.437, 0.52, 0.437], [0.438, 0.525, 0.635, 0.712, 0.755, 0.752, 0.682, 0.583, 0.52, 0.319, 0.319], [0.26, 0.357, 0.475, 0.562, 0.669, 0.712, 0.633, 0.525, 0.437, 0.319, 0.132]]]

#Set risk, how risky the computer player will be, lower = more risky
risk = 0.7
#Set increment, how much better the probability of not busting must be compared to the threshold
increment = 0.01
#Set scoring standards for columns
#Best
twoScore = 40
threeScore = 25.5
fourScore = 18.7
fiveScore = 13.5
sixScore = 11.1
sevenScore = 9.2
scoreDict = {0:twoScore,1:threeScore,2:fourScore,3:fiveScore,4:sixScore,5:sevenScore,6:sixScore,7:fiveScore,8:fourScore,9:threeScore,10:twoScore}
rangeDict = {0:0,1:1,2:1,3:2,4:2,5:3,6:2,7:2,8:1,9:1,10:0}
#open column array initialization
openCols = [True for i in range(0,11)]
#Column computer won on for testMode
winColTotal = [0 for i in range(0,11)]

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
def checkCol(col, board):
    open = checkOpen(col,board)
    if open == 2:
        for row in range(0,13):
            if board[col][12-row]%2 == 1:
                return (12-row) + 1
        return 0
    elif open == 1:
        if col == 0 or col == 10:
            return 2
        if col == 1 or col == 9:
            return 4
        if col == 2 or col == 8:
            return 6
        if col == 3 or col == 7:
            return 8
        if col == 4 or col == 6:
            return 10
        if col == 5:
            return 12
    else:
        return -1

#Function to check where the topmost marker is in a column for all players
def checkColAll(col, board):
    open = checkOpen(col,board)
    if open == 2:
        for row in range(0,13):
            if board[col][12-row] > 1:
                return (12-row) + 1
        return -10
    
#Function to check if a column is still open or if a player has reached the top of it
#0 means not open, 1 means not open because the computer is at top, and 2 means open
def checkOpen(col,board):
    if col == 0 or col == 10:
        if board[col][2] == 1:
            return 1
        elif board[col][2] != 0:
            return 0
    elif col == 1 or col == 9:
        if board[col][4] == 1:
            return 1
        elif board[col][4] != 0:
            return 0
    elif col == 2 or col == 8:
        if board[col][6] == 1:
            return 1
        elif board[col][6] != 0:
            return 0
    elif col == 3 or col == 7:
        if board[col][8] == 1:
            return 1
        elif board[col][8] != 0:
            return 0
    elif col == 4 or col == 6:
        if board[col][10] == 1:
            return 1
        elif board[col][10] != 0:
            return 0
    elif col == 5:
        if board[col][12] == 1:
            return 1
        elif board[col][12] != 0:
            return 0
    return 2

#Function to evaluate the roll for the computer player
def evalRoll(roll, mark1, mark2, mark3, board):
    #Pair dice
    pair1, pair2, pair3, pair4, pair5, pair6 = pairDice(roll)
    pairs = [pair1, pair2, pair3, pair4, pair5, pair6]
    #Set up temporary mark and score values
    rollScoreTemp = [0 for i in range(0,3)]
    mark1Temp = [0 for i in range(0,3)]
    mark2Temp = [0 for i in range(0,3)]
    mark3Temp = [0 for i in range(0,3)]
    #Evaluate the combinations
    for i in range (0,3):
        boardTemp = copy.deepcopy(board)
        mark1Temp[i], mark2Temp[i], mark3Temp[i], rollScoreTemp[i] = evalPair(pairs[2*i], pairs[2*i+1], mark1, mark2, mark3, boardTemp)
    if not testMode:
        print("Roll score is: ", rollScoreTemp)
    if rollScoreTemp == [0,0,0]:
        return [0,0],[0,0],[0,0],0
    index = rollScoreTemp.index(max(rollScoreTemp))
    if not testMode:
        print("The computer chose %d" %pairs[2*index], end='')
        print(" and %d" %pairs[2*index+1])
    if mark1[1] + 2 == mark1Temp[index][1] or mark2[1] + 2 == mark2Temp[index][1] or mark3[1] + 2 == mark3Temp[index][1]:
        double = 2
    else:
        double = 1
    mark1 = mark1Temp[index]
    mark2 = mark2Temp[index]
    mark3 = mark3Temp[index]
    return mark1, mark2, mark3, double
    
    #Function to evaluate the score of each pair
def evalPair(pair1, pair2, mark1, mark2, mark3, boardTemp):
    #Set the roll score to be 0
    rollScore = 0
    rollScore1 = 0
    rollScore2 = 0
    #Initialize temporary marks
    mark3Temp1 = mark3
    mark3Temp2 = mark3
    #If the pairs are the same
    if pair1 == pair2:
        #See if the first marker is open or the pairs match marker 1
        if mark1[1] == -1 or pair1 == (mark1[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark1 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark1,board)
            boardTemp[pair1-2][mark1[1]] += 1
            if checkOpen(pair2-2,boardTemp) == 2:
                mark1 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark1,board)
            boardTemp[pair1-2][mark1[1]-1] -= 1
        #See if the second marker is open or the pairs match marker 2
        elif mark2[1] == -1 or pair1 == (mark2[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark2 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark2,board)
            boardTemp[pair1-2][mark2[1]] += 1
            if checkOpen(pair2-2,boardTemp) == 2:
                mark2 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark2,board)
            boardTemp[pair1-2][mark2[1]-1] -= 1
        #See if the third marker is open or the pairs match marker 3
        elif mark3[1] == -1 or pair1 == (mark3[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark3 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark3,board)
            boardTemp[pair1-2][mark3[1]] += 1
            if checkOpen(pair2-2,boardTemp) == 2:
                mark3 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark3,board)
            boardTemp[pair1-2][mark3[1]-1] -= 1
    #If it's the first roll and the pairs are different then simply place the two markers
    elif mark1[1] == -1 and pair1 != pair2:
        if checkOpen(pair1-2,boardTemp) == 2:
            mark1 = [pair1-2,checkCol(pair1-2, boardTemp)]
            rollScore += evalCol(mark1,board)
        if checkOpen(pair2-2,boardTemp) == 2:
            if mark1[1] != -1:
                mark2 = [pair2-2,checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark2,board)
            else:
                mark1 = [pair2-2,checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark1,board)
    #If the second marker is open the pairs are different
    elif mark2[1] == -1 and pair1 != pair2:
        if pair1 == (mark1[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark1 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark1,board)
            if mark1[1] != -1:
                if checkOpen(pair2-2,boardTemp) == 2:
                    mark2 = [pair2-2, checkCol(pair2-2, boardTemp)]
                    rollScore += evalCol(mark2,board)
            else:
                if checkOpen(pair2-2,boardTemp) == 2:
                    mark1 = [pair2-2, checkCol(pair2-2, boardTemp)]
                    rollScore += evalCol(mark1,board)
        elif pair2 == (mark1[0] + 2):
            if checkOpen(pair2-2,boardTemp) == 2:
                mark1 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark1,board)
            if mark1[1] != -1:
                if checkOpen(pair1-2,boardTemp) == 2:
                    mark2 = [pair1-2, checkCol(pair1-2, boardTemp)]
                    rollScore += evalCol(mark2,board)
            else:
                if checkOpen(pair2-2,boardTemp) == 2:
                    mark1 = [pair2-2, checkCol(pair2-2, boardTemp)]
                    rollScore += evalCol(mark1,board)
        else:
            if checkOpen(pair1-2,boardTemp) == 2:
                mark2 = [pair1-2,checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark2,board)
            if mark2[1] != -1:
                if checkOpen(pair2-2,boardTemp) == 2:
                    mark3 = [pair2-2,checkCol(pair2-2, boardTemp)]
                    rollScore += evalCol(mark3,board)
            else:
                if checkOpen(pair2-2,boardTemp) == 2:
                    mark2 = [pair2-2, checkCol(pair2-2, boardTemp)]
                    rollScore += evalCol(mark2,board)
    #If the third marker is open and pairs are different, check the first pair first
    elif mark3[1] == -1:
        if pair1 == (mark1[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark1 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark1,board)
        elif pair1 == (mark2[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark2 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark2,board)
        else:
            if checkOpen(pair1-2,boardTemp) == 2:
                mark3Temp1 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore1 += evalCol(mark3Temp1,board)
        #Then check pair2
        if pair2 == (mark1[0] + 2):
            if checkOpen(pair2-2,boardTemp) == 2:
                mark1 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark1,board)
        elif pair2 == (mark2[0] + 2):
            if checkOpen(pair2-2,boardTemp) == 2:
                mark2 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark2,board)
        else:
            if checkOpen(pair2-2,boardTemp) == 2:
                mark3Temp2 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore2 += evalCol(mark3Temp2,board)
        #Check to see which pair placed better then record that pair and score
        if rollScore1 >= rollScore2:
            mark3 = mark3Temp1
            rollScore += rollScore1
        else:
            mark3 = mark3Temp2
            rollScore += rollScore2
    #Otherwise try to match the pairs to the existing marks
    else:
        #See if either pair matches the first marker
        if pair1 == (mark1[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark1 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark1,board)
        elif pair2 == (mark1[0] + 2):
            if checkOpen(pair2-2,boardTemp) == 2:
                mark1 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark1,board)
        #See if either pair matches the second marker
        if pair1 == (mark2[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark2 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark2,board)
        elif pair2 == (mark2[0] + 2):
            if checkOpen(pair2-2,boardTemp) == 2:
                mark2 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark2,board)
        #See if either pair matches the third marker
        if pair1 == (mark3[0] + 2):
            if checkOpen(pair1-2,boardTemp) == 2:
                mark3 = [pair1-2, checkCol(pair1-2, boardTemp)]
                rollScore += evalCol(mark3,board)
        elif pair2 == (mark3[0] + 2):
            if checkOpen(pair2-2,boardTemp) == 2:
                mark3 = [pair2-2, checkCol(pair2-2, boardTemp)]
                rollScore += evalCol(mark3,board)
    #Give a bonus depending on how many extra markers are left if the player didn't bust
    if rollScore > 0:
        if mark2[1] == -1:
            rollScore += 2000
        elif mark3[1] == -1:
            rollScore += 1000
    return mark1, mark2, mark3, rollScore

#Function to evalutate the score of a single column
def evalCol(mark,board):
    score = 0
    #Give score for current position on column
    score += scoreDict[mark[0]]*(mark[1]+1)
    if not testMode:
    #Check to see where the leading player is on that column
        leader = checkColAll(mark[0],board)
        range = rangeDict[mark[0]]
        if mark[1] <= leader+range and mark[1] >= leader-range:
            score += 15
            print("In range")
        if mark[1] < leader-range:
            score -= 20
            print("Out of range")
    if score < 1:
        score = 1
    return score

def evalRollAgain(mark1, mark2, mark3, openCols, reward):
    if mark1[1] == -1 or mark2[1] == -1 or mark3[1] == -1:
        return True
    elif checkOpen(mark1[0],board) != 2 and checkOpen(mark2[0],board) != 2:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round(prob1[mark3[0]],4))
            print("Threshold is: ", round(risk + increment*reward,4))
        if prob1[mark3[0]] > (risk + increment*reward):
            return True
        else:
            return False
    elif checkOpen(mark1[0],board) != 2 and checkOpen(mark3[0],board) != 2:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round(prob1[mark2[0]],4))
            print("Threshold is: ", round(risk + increment*reward,4))
        if prob1[mark2[0]] > risk + increment*reward:
            return True
        else:
            return False
    elif checkOpen(mark2[0],board) != 2 and checkOpen(mark3[0],board) != 2:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round((prob1[mark1[0]]),4))
            print("Threshold is: ", round((risk + increment*reward),4))
        if prob1[mark1[0]] > (risk + increment*reward):
            return True
        else:
            return False
    elif checkOpen(mark1[0],board) != 2:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round(prob2[mark2[0]][mark3[0]],4))
            print("Threshold is: ", round(risk + increment*reward,4))
        if prob2[mark2[0]][mark3[0]] > (risk + increment*reward):
            return True
        else:
            return False
    elif checkOpen(mark2[0],board) != 2:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round(prob2[mark1[0]][mark3[0]],4))
            print("Threshold is: ", round(risk + increment*reward,4))
        if prob2[mark1[0]][mark3[0]] > (risk + increment*reward):
            return True
        else:
            return False
    elif checkOpen(mark3[0],board) != 2:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round(prob2[mark1[0]][mark2[0]],4))
            print("Threshold is: ", round(risk+increment*reward,4))
        if prob2[mark1[0]][mark2[0]] > (risk + increment*reward):
            return True
        else:
            return False
    else:
        if not testMode:
            print("Reward is: ", reward)
            print("Probability of not busting is: ", round(prob3[mark1[0]][mark2[0]][mark3[0]],4))
            print("Threshold is: ", round(risk + increment*reward,4))
        if prob3[mark1[0]][mark2[0]][mark3[0]] > (risk + increment*reward):
            return True
        else:
            return False

def checkGameOver(winCol,board):
    win = 0
    for col in range(0,11):
        if checkOpen(col,board)%2 == 1:
            win += 1
        if win >= 3:
            for col in range(0,11):
                if checkOpen(col,board)%2 == 1:
                    winCol[col] += 1
            return True, winCol
    return False, winCol
#------------------------------------------------------#

#-------------------------Main----------------------------#

#Game beginning
print("Welcome to the Can't Stop AI")

while True:
    #Set test mode if desired, this is for optimizing the computer's values
    test = input("Would you like to use test mode? Enter y for yes or n for no, then hit enter. ")
    if test == 'y':
        testMode = True
        break
    if test == 'n':
        testMode = False
        break

if testMode:
    #Initialize the total number of rounds and busts to 0
    roundTotal = 0
    bustTotal = 0
    while True:
        try:
            gameNumber = int(input("Input the number of games you would like the computer to play. "))
        except ValueError:
            print("Please input a number!")
            continue
        if gameNumber > 0:
            break
        else:
            print("Please input a positive number")
            continue
else:
    gameNumber = 1
    
gameInitial = gameNumber
#While there is still another game to play
while gameNumber > 0:
    
    #Initialization for the game
    winCol = [0 for i in range(0,11)]
    #Set the turn to be the first player's turn
    turn = 1
    #Set the game to be not over
    gameOver = False
    #Create the board
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
    #If on test mode for computer optimization
    if testMode:
        #Set the turn to be the computer's turn
        turn = 0
        #Set the number of rounds that have occurred
        round = 0
        #Set the number of busts that the computer occured
        busts = 0
    if not testMode:
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
    while not gameOver:
        if testMode:
            turn = 0
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
            
            #Check for closed columns
            #for i in range(0,11):
            #   openCols[i] = checkOpen(i+2,board)
            #Increment the turn
            if turn < players:
                 turn += 1
            else:
                 turn = 0
        
        #Computer Player's turn
        while turn == 0:
            reward = 0
            if not testMode:
                print("Computer Player's turn")
            if testMode:
                round += 1
            #Initalize the markers and pairs
            mark1 = [-1,-1]
            mark2 = [-1,-1]
            mark3 = [-1,-1]
            boardSave = copy.deepcopy(board)
            rollAgain = True
            rollNumber = 1
            while rollAgain:
                if not testMode:
                    print("Roll ", rollNumber)
                #Roll the dice
                roll = rollDice()
                ### Debugging roll maker
                #roll = [0,0,0,0]
                #roll[0] = int(input("First Roll: "))
                #roll[1] = int(input("Second Roll: "))
                #roll[2] = int(input("Third Roll: "))
                #roll[3] = int(input("Fourth Roll: "))
                ###
                if not testMode:
                    print("Computer's roll is: ", roll)
                #Evaluate roll
                mark1, mark2, mark3, double = evalRoll(roll, mark1, mark2, mark3, board)
                if mark1 == [0,0] and mark2 ==[0,0] and mark3 == [0,0]:
                    board = boardSave
                    if not testMode:
                        print("Computer Busted")
                        printBoard(board)
                    if testMode:
                        busts += 1
                    break
                #Finalize the output
                if mark1[1] != -1:
                    if board[mark1[0]][mark1[1]]%2 == 0:
                        board[mark1[0]][mark1[1]] += 1
                        reward += scoreDict[mark1[0]]/10*double
                        for i in range(0,mark1[1]):
                            if board[mark1[0]][i]%2 == 1:
                                board[mark1[0]][i] -= 1
                if mark2[1] != -1:
                    if board[mark2[0]][mark2[1]]%2 == 0:
                        board[mark2[0]][mark2[1]] += 1
                        reward += scoreDict[mark2[0]]/10*double
                        for i in range(0,mark2[1]):
                            if board[mark2[0]][i]%2 == 1:
                                board[mark2[0]][i] -= 1
                if mark3[1] != -1:
                    if board[mark3[0]][mark3[1]]%2 == 0:
                        board[mark3[0]][mark3[1]] += 1
                        reward += scoreDict[mark3[0]]/10*double
                        for i in range(0,mark3[1]):
                            if board[mark3[0]][i]%2 == 1:
                                board[mark3[0]][i] -= 1
                if not testMode:
                    print("mark1 = ", mark1)
                    print("mark2 = ", mark2)
                    print("mark3 = ", mark3)
                    printBoard(board)
                rollAgain = evalRollAgain(mark1, mark2, mark3, openCols, reward)
                rollNumber += 1
                if not testMode:
                    input("Hit enter to continue")
                gameOver,winCol = checkGameOver(winCol,board)
                if gameOver == True:
                    rollAgain = False
            turn = 1
    if testMode:
        #print(f"Computer won in {round} rounds.")
        roundTotal += round
        #print(f"Computer busted {busts} times.")
        bustTotal += busts
        gameNumber -= 1
        for col in range(0,11):
            winColTotal[col] += winCol[col]

#Final Results
if testMode:
    print("Risk is: ", risk)
    print("Increment is: ", increment)
    accuracy = 100*(1 - bustTotal/roundTotal)
    speed = (roundTotal/gameInitial)
    print(f"The computer player {gameInitial} games in {roundTotal} rounds and busted {bustTotal} times.")
    print(f"The computer had an accuracy of {accuracy:.1f}% and an average speed of {speed:.2f} rounds per game.")
    print("Winning columns were: ",winColTotal)
    #--------------------------------------------------------#
    