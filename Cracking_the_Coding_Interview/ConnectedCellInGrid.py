visited=[]
def search(G,v,count):
    # print "on: " + str(v[0])+"," + str(v[1])
    global visited
    i = v[0]
    j = v[1]
    tot=0
    neighbors=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
    visited.append(v)
    # print visited
    for neighbor in neighbors:
        if not checkVisited(neighbor) and isValid(neighbor,len(G),len(G[0])) and G[neighbor[0]][neighbor[1]]==1:
            # print "recurse at: " + str(neighbor[0])+"," + str(neighbor[1])
            tot = search(G,neighbor,count+1)
    return tot+1

def isValid(v,r,c):
    if v[0] < r and v[0] >=0 and v[1] <c and v[1] >=0:
        return True
    else:
        return False



def checkVisited(v):
    global visited
    for point in visited:
        if v[0] == point[0] and v[1] == point[1]:
            return True
    return False

def get_biggest_region(grid):
    tmax = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            v=[r,c]
            if not checkVisited(v) and grid[r][c]==1:
                temp = search(grid,v,0)
                # print temp
                if temp > tmax:
                    tmax = temp
    return tmax

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
