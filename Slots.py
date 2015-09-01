'''
Slot Machine Simulator by Keegan Bailey
10 spins,
6 symbols,
5 pay lines,
---
TODO: add Wilds, add Credits,
'''

import random
import math

reel = []
game = []
symbols = ["J","Q","K","A","7","$"]

def spin():
    '''Sets up a 3x5 grid for the symbols
'''
    global game
    game = [[None for x in range(5)] for x in range(3)]
    
    for x in range(3):
        for y in range(5):
            game[x][y] = reel[random.randint(100000, 600000) % 32]
         
def printGame():
    for i in game:
        print i

def printPayout(line, symb, count):
    ln = line+1
    print "Line: %d %s(%d) pays!!" % (ln, symb, count)

def payout():
    for i in range(5):
        symb, count = checkLine(i)
        if count > 1:
            printPayout(i, symb, count)

def checkLine(lineNum):
    y = [0,1,2,3,4]
    if lineNum == 0:
        # pos: 0,0 0,1 0,2 0,3 0,4
        x = [0,0,0,0,0]
    elif lineNum == 1:
        # pos: 1,0 1,1 1,2 1,3 1,4
        x = [1,1,1,1,1]
    elif lineNum == 2:
        # pos: 2,0 2,1 2,2 2,3 2,4
        x = [2,2,2,2,2]
    elif lineNum == 3:
        # pos: 0,0 1,1 2,2 1,3 0,4
        x = [0,1,2,1,0]
    elif lineNum == 4:
        # pos: 2,0 1,1 0,2 1,3 2,4
        x = [2,1,0,1,2]
    else:
        print "Error: No line exists"
    return checkSymbol(x, y)
    
def checkSymbol(x, y):
    count = 0
    for s in symbols:            
        if game[x[0]][y[0]] == s:
            count += 1
            symbol = s
            if game[x[1]][y[1]] == s:
                count += 1
                if game[x[2]][y[2]] == s:
                    count += 1
                    if game[x[3]][y[3]] == s:
                        count += 1
                        if game[x[4]][y[4]] == s:
                            count += 1
    return symbol, count

def getReel():
    '''Sets up probabilty of getting symbols:
       8x J's   7x Q's   6x K's
       5x A's   4x 7's   2x $'s
'''
    for i in range(32):
        if i < 8:
            reel.append("J")
        elif i >= 7 and i < 15:
            reel.append("Q")
        elif i >= 15 and i < 21:
            reel.append("K")
        elif i >= 21 and i < 26:
            reel.append("A")
        elif i >= 26 and i < 30:
            reel.append("7")
        else:
            reel.append("$")
    return reel

def runGame():
    spin()
    printGame()
    payout()

if __name__ == "__main__":
    print "Welcome to the Test Slot Machine"
    getReel()

    for i in range(10):
        runGame()
        print "----------"
    
