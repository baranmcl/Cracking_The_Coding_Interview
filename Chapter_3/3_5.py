'''
Implement a MyQueue class which implements a queue using two stacks.
'''

class MyQueue:
    def __init__(self):
        self.instack = []
        self.outstack = []
    def enqueue(self, item):
        self.instack.append(item)
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        
q = MyQueue()
for i in range(10):
    q.enqueue(i)
for i in range(10):
    print q.dequeue()
