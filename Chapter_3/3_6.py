'''
Write a program to sort a stack in ascending order (with biggest items on top). 
You may use at most one additional stack to hold items, 
but you may not copy the elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty.
'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    def printStack(self):
        print self.stack
    def bubbleSort(self):
        for i in xrange(len(self.stack)-1,0,-1):
            for j in xrange(i):
                if self.stack[j] > self.stack[j+1]:
                    self.stack[j], self.stack[j+1] = self.stack[j+1], self.stack[j]


myStack = Stack()
data = [1,9,2,3,8,1]
for i in data:
    myStack.push(i)
myStack.printStack()
myStack.bubbleSort()
myStack.printStack()
