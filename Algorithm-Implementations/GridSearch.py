#!/bin/python

import sys

def checkGrid(G,P,R,C,r,c):

    for i in range(R):
        for j in range(C):
            valid = True
            if G[i][j] == P[0][0] and j+c < C and i+r < R:
                for y in range(r):
                    for x in range(c):
                        if P[y][x] != G[i+y][j+x]:
                            valid=False;
                            break
                    if valid == False:
                        break
                if valid == True:
                    return 'YES'
    return 'NO'

t = int(raw_input().strip())
ans = []
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)
    ans.append(checkGrid(G,P,R,C,r,c))
#print answer
for i in ans:
    print i
