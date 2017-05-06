#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(n):
    line=""
    for j in range(n):
        if j >= (n-i-1):
            line+= "#"
        else:
            line+= " "
    print line
