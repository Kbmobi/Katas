def spiral(n):
    x, y, dx, dy = 0, 0, 0, -1

    for i in range(n**2):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
            dx, dy = -dy, dx 
        yield x, y
        x, y = x+dx, y+dy

def makeGrid(n):
    matrix = [[0 for x in range(n)] for x in range(n)]

    a = 0
    while a < n:
        b = 0
        for d in matrix[a]:
            matrix[a][b] = (a+1, b+1) 
            b += 1
        a += 1

    return matrix

        
if __name__ == "__main__":
    input1 = "3 8".split()

    magic = int(input1[0])
    m = makeGrid(int(input1[0]))
    x = list(spiral(int(input1[0])))

    for i in x:
        print m[i[0]+(magic/2)][i[1]+(magic/2)]



'''

3
8
output:(2,3)

7
1 1

'''
