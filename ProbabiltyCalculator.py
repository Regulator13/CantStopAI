#Can't Stop Probability

#Libraries
from random import randint
#Finding the probabilty of rolling a 7 with 4 dice

def rollDice():
    roll = [0,0,0,0]
    for i in range (0,4):
        roll[i] = randint(1,6)
    return roll

def pairDice(roll):
    #pair all posibilities
    pairs = [roll[0] + roll[1], roll[2] + roll[3], roll[0] + roll[2], roll[1] + roll[3], roll[0] + roll[3], roll[1] + roll[2]]
    return pairs

#Counts the number shown on the dice for a given number of rolls
def countRoll():
    for k in range(0,1000):
        roll = rollDice()
        for l in range(0,4):
            countRoll[roll[l]-1] += 1
    print(countRoll)

#Counts the number of pairs (2-12) for the given number of rolls
def countPairs():
    for i in range(0,10000):
        roll = rollDice()
        pairs = pairDice(roll)
        for j in range (0,6):
            count[pairs[j]-2] += 1
    print(count)

#Counts the number of rolls that have at least 1 pair equal to each number (1 marker)
def count1Marker():
    for i in range(0,1000):
        roll = rollDice()
        pairs = pairDice(roll)
        for j in range(0,11):
            for k in range(0,6):
                if pairs[k] == (j+2):
                    count[j] += 1
                    break
    print(count)

#Counts the number of rolls that have at least 1 pair equal to 1 of 2 numbers (2 markers)
def count2Marker():
    for i in range(0,1000000):
        roll = rollDice()
        pairs = pairDice(roll)
        for j in range(0,11):
            for k in range(0,11):
                for l in range(0,6):
                    if pairs[l] == (j+2) or pairs[l] == (k+2):
                        count2[j][k] += 1
                        break
    return count2

def printCount2(count2):
    for i in range(3,13):
        print("2,%d is "%i, end=' ')
        print(count2[0][i-2])
    print()
    for i in range(4,13):
        print("3,%d is "%i, end=' ')
        print(count2[1][i-2])
    print()
    for i in range(5,13):
        print("4,%d is "%i, end=' ')
        print(count2[2][i-2])
    print()
    for i in range(6,13):
        print("5,%d is "%i, end=' ')
        print(count2[3][i-2])
    print()
    for i in range(7,13):
        print("6,%d is "%i, end=' ')
        print(count2[4][i-2])
    print()
    for i in range(8,13):
        print("7,%d is "%i, end=' ')
        print(count2[5][i-2])
    print()
    for i in range(9,13):
        print("8,%d is "%i, end=' ')
        print(count2[6][i-2])
    print()
    for i in range(10,13):
        print("9,%d is "%i, end=' ')
        print(count2[7][i-2])
    print()
    for i in range(11,13):
        print("10,%d is "%i, end=' ')
        print(count2[8][i-2])
    print()
    for i in range(12,13):
        print("11,%d is "%i, end=' ')
        print(count2[9][i-2])
    print()

#Counts the number of rolls that have at least 1 pair equal to 1 of 3 numbers (3 markers)
def count3Marker():
    for i in range(0,1000000):
        roll = rollDice()
        pairs = pairDice(roll)
        for j in range(0,11):
            for k in range(0,11):
                for l in range(0,11):
                    for m in range(0,6):
                        if pairs[m] == (j+2) or pairs[m] == (k+2) or pairs[m] == (l+2):
                            count3[j][k][l] += 1
                            break
    return count3


#--------------Main Loop---------------------#
countRoll = [0,0,0,0,0,0]
count = [0,0,0,0,0,0,0,0,0,0,0]
count2 = [[0 for i in range(0,11)] for j in range(0,11)]
count3 = [[[0 for i in range(0,11)] for j in range(0,11)] for k in range(0,11)]

count3 = count3Marker()
print(count3)
