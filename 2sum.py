# Given an arbitrary number, return a set of all subsets of two numbers that will add up to the value
import sys

def twoSum(val):
    num = int(val)
    k  = num/2+1
    i = 0
    fullSet=[]
    for i in range(k):
        subset=[]
        subset.append(i)
        subset.append(num-i)
        fullSet.append(subset)
    return fullSet

def threeSum(val):
    num = int(val)
    k  = num/2+1
    fullSet = []
    for i in range(num):
        subset1 = []
        subset1.append(i)
        fullSet.append(subset1)
    for s in fullSet:
        for n in range(k):
            s.append(n)
            s.append(num-n)
    return fullSet

input = sys.argv[1]
# print(twoSum(input))

print(threeSum(input))
