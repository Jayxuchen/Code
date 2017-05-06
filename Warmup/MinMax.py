#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
arr = sorted(arr)
print str(sum(arr[:4])) +" "+ str(sum(arr[1:]))
