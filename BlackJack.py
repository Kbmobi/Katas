import random

stack = []
playerHand = []
dealerHand = []

def deck():
    suits = 'S C H D'.split() 
    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    deck = [r + s for s in suits for r in ranks]

    random.shuffle(deck)

    for i in deck:
        stack.append(i)

def draw(hand):
    try:
        hand.append(stack.pop())
    except IndexError:
        deck()
        hand.append(stack.pop())
    
def evaluate(hand):
    ace = False # if the total is < 12 add 10 to total
    total = 0
    
    for i in hand:
        if "10" or "J" or "Q" or "K" in i:
            total += 10
        if "A" in i:
            total += 1
            ace = True
        else:
            total +=  int(i[:-1])

    if total < 12 and ace == True:
        return total+10
    else:
        return total

def clear():
    playerHand = []
    dealerHand = []

def setupGame():
    deck()

if __name__ == '__main__':
    setupGame()

    
