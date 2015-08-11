def spiral(n, m = 0, arg1 = 0, arg2 = 0):
    x, y, dx, dy = 0, 0, 0, -1

    count = 1
    for i in range(n**2):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
            dx, dy = -dy, dx 
        
        tp1, tp2 = pos(n, x, y)
        if arg1 == tp1 and arg2 == tp2:
            print "(%d, %d) found at number %d" % (tp1, tp2, count)
        
        if count == m and m > 0:
            print "%d pos = (%d, %d)" % (m, tp1, tp2)
            
        count += 1
        
        yield x, y
        x, y = x+dx, y+dy

def pos(n, x, y):
    return (n/2+1) + x, (n/2+1) + y

if __name__ == "__main__":
    print list(spiral(3,8))
    

'''

3
8


7
1 1

'''
