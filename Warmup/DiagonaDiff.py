#!/bin/python

import sys

def getDiagonalDifference(arr,rows):
    diag=[0,0]
    for a in range(rows):
        diag[0]+=arr[a][a]
        diag[1]+=arr[a][rows-1-a]
    return abs((diag[0]-diag[1]))
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

print getDiagonalDifference(a,n)
