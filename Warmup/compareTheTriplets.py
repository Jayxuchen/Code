#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    pts = [0,0]
    a=[a0,a1,a2]
    b=[b0,b1,b2]
    for i,j in zip(a,b):
        if i > j:
            pts[0]+=1
        elif i < j:
            pts[1]+=1
    return pts

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
