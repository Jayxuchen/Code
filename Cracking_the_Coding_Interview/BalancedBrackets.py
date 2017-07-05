class Stack(object):
    def __init__(self):
        self.ar = []
    def push(self,e):
        self.ar.insert(0,e)
    def pop(self):
        v = self.ar[0]
        #needs to remove first element
        self.ar.delete(0)
        return v

def is_matched(expression):
    stack = Stack()
    for a in expression:
        print a
        if a is "[" or a is "(" or a is "{":
            stack.push(a)
        else:
            k = stack.pop()
            if a is ']':
                if k is not '[':
                    return False
            elif a is ')':
                if k is not '(':
                    return False
            else:
                if k is not '{':
                    return False
    return True
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
