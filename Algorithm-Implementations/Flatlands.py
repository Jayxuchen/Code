#!/bin/python

import sys

def getMaxDistance(n,stations):

    sortedArr = quicksort(stations)

    maxDist = sortedArr[0]
    for i in range(len(sortedArr)-1):
        dist = (sortedArr[i+1]-sortedArr[i])/2
        if dist > maxDist:
            maxDist = dist
    dist = ((n-1) - sortedArr[len(sortedArr)-1])
    if dist > maxDist:
        maxDist = dist
    return maxDist


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

print getMaxDistance(n,c)
