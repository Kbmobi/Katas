# Single Deck Blackjack Simulator :: By Keegan Bailey
# The simulator will follow basic stratagy for player (excluding splits), dealer stands on soft 17
import random

playerWon = 0
houseWon = 0
push = 0
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
        if "10" in i:
            total += 10
        elif "J" in i:
            total += 10
        elif "Q" in i:
            total += 10
        elif "K" in i:
            total += 10
        elif "A" in i:
            total += 1
            ace = True
        else:
            total +=  int(i[:-1])
    
    if total < 12 and ace == True:
        return total+10
    else:
        return total

def clear():
    del playerHand[:]
    del dealerHand[:]

def deal():
    draw(playerHand)
    draw(dealerHand)
    draw(playerHand)
    draw(dealerHand)
    gameover = playerGame()
    if gameover == False:
        dealerGame()
    end()

def end():
    global playerWon
    global houseWon
    global push
    dealer = evaluate(dealerHand)
    player = evaluate(playerHand)
    print "DealerHand: %s -- Total:%s" % (dealerHand, str(dealer))
    print "PlayerHand: %s -- Total:%s" % (playerHand, str(player))

    if player == dealer:
        push += 1
        print "Push"
    elif player < 22 and player > dealer or dealer > 21:
        playerWon += 1
        print "Player wins"
    else:
        houseWon += 1
        print "House wins"
    print "----------------------------"
    
    clear()

def dealerGame():
    while evaluate(dealerHand) < 17:
        draw(dealerHand)

def playerGame():
    #player goes before dealer. dealer will only play if player does not bust. dealer will not play again a blackjack unless they have an ace
    dealer = evaluate(dealerHand[:-1])
    if evaluate(playerHand) == 21:
        if dealer == 11:
            return False
        return True
    
    while evaluate(playerHand) < 12:
        draw(playerHand)

    if dealer < 7:
        return False
    else: #dealer > 6
        while evaluate(playerHand) < 17:
            draw(playerHand)

    if evaluate(playerHand) > 21:
        return True
    
    return False

if __name__ == '__main__':
    x = input("How many hands do you want to simulate?: ")

    i = 0
    while i < x:
        print "Game #%d" % (i + 1)
        deal()
        i += 1

    print "Total:  Hands: %d \nPlayer: %d - House: %d - Push %d"  % (i, playerWon, houseWon, push)    
