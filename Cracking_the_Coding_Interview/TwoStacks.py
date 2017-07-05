
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
    #pop all elements into second stack, return first element of second stack
    #O(n)
    def pop(self):
    #pop all elements into second stack
    #pop first element of second stack for return
    #pop all other elements back into first stack
    #O(2n)

    def put(self, value):
    #Push into first stack
    #O(1)
    
queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
