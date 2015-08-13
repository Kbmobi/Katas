#Challenge #227 [Easy] Square Spirals
#https://www.reddit.com/r/dailyprogrammer/comments/3ggli3/20150810_challenge_227_easy_square_spirals/
#Solution by Keegan Bailey

def spiral(n):
    x = 0
    y = 0
    dx = 0
    dy = -1

    for i in range(n**2):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
            dx, dy = -dy, dx 
        yield x, y
        x, y = x+dx, y+dy

def makeGrid(n):
    matrix = [[0 for g in range(n)] for g in range(n)]

    y = 0
    while y < n:
        x = 0
        for d in matrix[y]:
            matrix[y][x] = (x+1, y+1) 
            x += 1
        y += 1

    return matrix

def getArrayPoint(m, x, y):
    middle = len(m)/2
    rx = middle + x
    ry = middle + -y
    return m[ry][rx]     

def getByNumber(m, s, n):
    return getArrayPoint(m,s[n-1][0],s[n-1][1])
    

def getByQuard(m, s, x, y):
    count = 1
    for i in s:
        point = getArrayPoint(m, i[0], i[1])
        if point[0] == x and point[1] == y:
            return count
        count += 1

def run(ui):
    if len(ui) <= 0:
        return
    
    m = makeGrid(int(ui[0]))
    s = list(spiral(int(ui[0])))
    
    if len(ui) == 3:
        return getByQuard(m, s, int(ui[1]), int(ui[2]))
    else:
        return getByNumber(m, s, int(ui[1]))
        
        
if __name__ == "__main__":
    ex1 = "3 8".split()
    ex2 = "7 1 1".split()
    ex3 = "11 50".split()
    ex4 = "9 6 8".split()
    # Memory Error
    #ex5 = "1024716039 557614022".split()
    #ex6 = "234653477 11777272 289722".split()

    print run(ex1)
    print run(ex2)
    print run(ex3)
    print run(ex4)
    #print run(ex5)
    #print run(ex6)

'''

Expected Output:
(2,3)
37
(10, 9)
47
(512353188, 512346213)
54790653381545607

'''
