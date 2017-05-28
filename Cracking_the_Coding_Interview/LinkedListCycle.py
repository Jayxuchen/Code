"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    curr = head
    mydict = []
    while curr is not None:
        if str(curr) in mydict:
            return True
        mydict.append(str(curr))
        # print mydict
        curr = curr.next
    return False
