'''
Slot Machine Simulator by Keegan Bailey
10 spins,
6 symbols,
5 pay lines,
Has Credits,
Raise/lower bets,
Paytable
---
TODO: add Wilds
'''

import random

reel = []
game = []
symbols = ["J","Q","K","A","7","$"]
creds = 10000
bet = 100

def spin():
    global game
    global creds

    creds = creds - bet
    game = [["X" for x in range(5)] for x in range(3)]
    
    for x in range(3):
        for y in range(5):
            game[x][y] = reel[random.randint(100000, 600000) % 32]
         
def printGame():
    for i in game:
        print i
    print "Credits: %d    Bet: %d" % (creds, bet)
        
def printPayTable():
    print "Pay Table: Per Credit Bet!"
    print "JJJ   = 10   QQQ   = 20    KKK   = 30"
    print "JJJJ  = 100  QQQQ  = 200   KKKK  = 300"
    print "JJJJJ = 1000 QQQQQ = 2000  KKKKK = 3000"
    print "AAA   = 50   777   = 100   $$$   = 1000"
    print "AAAA  = 500  7777  = 1000  $$$$  = 10000"
    print "AAAAA = 5000 77777 = 50000 $$$$$ = 100000"
    print "-----------------------------------------"
    raw_input("Press enter to continue.")
    printIntro()

def printIntro():
    print "Welcome to Python Slots!"
    print "['7', '7', '7', '7', '7']"
    print "['$', '7', '7', '7', '$']"
    print "['$', '$', '7', '$', '$']"
    print "Credits: %d    Bet: %d" % (creds, bet)

def printPay(pay, c, s):
    print "Won %d!! %dx %s's" % (pay, c, s)

def raiseBet():
    global bet
    if bet + 100 <= creds:
        bet = bet + 100
    printIntro()

def lowerBet():
    global bet
    if bet - 100 >= 0:
        bet = bet - 100
    printIntro()

def getPayout(s, c):
    if s == "J":
            pay = bet * (10 ** (c-2))
    elif s == "Q":
            pay = bet * (20 ** (c-2))
    elif s == "K":
            pay = bet * (30 ** (c-2))
    elif s == "A":
            pay = bet * (50 ** (c-2))
    elif s == "7":
            pay = bet * (100 ** (c-2))
    elif s == "$":
            pay = bet * (1000 ** (c-2))
    printPay(pay, c, s)
    adjustCredits(pay)

def adjustCredits(p):
    global creds
    creds = creds + p
    
def payout():
    for i in range(5):
        symb, count = checkLine(i)
    if count > 2:
        getPayout(symb, count)

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
       5x A's   4x 7's   2x $'s'''
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
    
def setup():
    getReel()
    printIntro()
    
def runGame():
    spin()
    payout()
    printGame()

def getInput():
    x = None
    while 1:
        if x == "P":
            printPayTable()
            x = None
        elif x == "U":
            raiseBet()
            x = None
        elif x == "L":
            lowerBet()
            x = None
        elif x == "S":
            print "------------------"
            runGame()
            x = None
        elif x == "Q":
            print "Thanks for playing!"
            return
        elif x == "M":
            for x in range(int(raw_input("How Many Spins?: "))):
                print "------------------"
                runGame()
            x = None
        else:
            x = raw_input("Quit:(Q)|PayTable:(P)\nRaiseBet:(U)|LowerBet(L)|Spin(S)\nMultiSpin:(M) : ")
        

if __name__ == "__main__":
    setup()
    getInput()
    
