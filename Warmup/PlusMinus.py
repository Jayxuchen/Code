#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
vals=[0,0]
for i in arr:
    if i > 0:
        vals[0]+=1
    if i < 0:
        vals[1]+=1

print vals[0]/float(n)
print vals[1]/float(n)
print (n-vals[0]-vals[1])/float(n)
