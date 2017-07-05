#!/bin/python

import sys

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def addToTree(root,data):
    curr = root
    while curr is not None:
        if data < curr.data:
            curr = root.left
        else:
            curr = root.right
    curr = Node(data)



n = int(raw_input().strip())
a = []
a_i = 0
a_t = int(raw_input().strip())
root = Node(a_t)
for a_i in xrange(n-1):
    a_t = int(raw_input().strip())
    a.append(a_t)
