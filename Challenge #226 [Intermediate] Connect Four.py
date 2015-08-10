#https://www.reddit.com/r/dailyprogrammer/comments/3fva66/20150805_challenge_226_intermediate_connect_four/
#Solution by Keegan Bailey
    
def DropPiece(position):
    player = getPlayer(turnNumber)
    
    count = columns - 1
    while count >= 0:
        if(playTable[count][position] == "."):
            playTable[count][position] = player
            break
        count -= 1
    return player, count, position

def getPlayer(turnNumber):
    if(turnNumber % 2 == 0):
        return player1
    else:
        return player2

def CheckForWinner(player, x, y):
    solution = str(x)+str(y)
    for toCheck in checkableArea:
        cRow, cCol = toCheck  
        if(OutOfBoundsCheck(x+cRow, y+cCol) == True):
            continue
        
        if(playTable[x+cRow][y+cCol] == player):
            solution += ", "+str(x+cRow)+str(y+cRow)
            if(OutOfBoundsCheck(x+(cRow*2),y+(cCol*2)) == True):
                continue
            
            if(playTable[x+(cRow*2)][y+(cCol*2)] == player):
                solution += ", "+str(x+(cRow*2))+str(y+(cCol*2))
                
                if(OutOfBoundsCheck(x+(cRow*3),y+(cCol*3)) == True):
                    continue
                
                if(playTable[x+(cRow*3)][y+(cCol*3)] == player):
                    solution += ", "+str(x+(cRow*3))+str(y+(cCol*3))
                    return player, solution   
    return None, solution

def OutOfBoundsCheck(x, y):
    if(x < 0 or x > rows - 2):
        return True;
    if(y < 0 or y > columns - 1):
        return True;
    return False
        
      
       

if __name__ == "__main__":
    player1 = "X"
    player2 = "O"
    
    columns = 6
    rows = 7
    checkableArea = [(-1, -1), (0, -1), (-1, 0), (1, 1), (0, 1), (1, 0), (-1, 1), (1, -1)]
    playTable = [["." for x in range(rows)] for y in range(columns)]
    playerMoves = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6}
    
    winner = None
    solution = ""
    fullGame = ["C","d","D","d","D","b","C","f","C","c","B","a","A","d","G","e","E","g"]
    turnNumber = 0
    
    while turnNumber < len(fullGame):      
        player, x, y = DropPiece(playerMoves[fullGame[turnNumber].lower()])
        winner, solution = CheckForWinner(getPlayer(turnNumber), x, y)
        turnNumber += 1
        if winner != None:
            break

    for i in playTable:
        print i

    print winner + " won on turn " + str(turnNumber/2+1) + " with (" +solution + ")"
