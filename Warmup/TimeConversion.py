#!/bin/python

import sys


time = raw_input().strip()

ar = time.split(":")


if ar[2][2:] == 'PM':
    if ar[0] !="12":
        ar[0] = str(int(ar[0])+12)
else:
    if ar[0]=="12":
        ar[0]="00"
ar[2]=ar[2][:2]
print ":".join(ar)
