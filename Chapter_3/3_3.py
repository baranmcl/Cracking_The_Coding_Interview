'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOf Stacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if ther ewere just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''
'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class SetOfStacks:
    def __init__(self, limit=None):
        self.stacks = []
        self.limit = limit
        self.toLimit = limit
    def push(self, stack):
        #if stack size is <= toLimit
        if stack.size() <= self.toLimit:
            self.stacks.append(stack)
            self.toLimit -= stack.size()
        #if stack size is > toLimit
        else:
            tempdata = []
            #if first stack is greater than limit
            if len(self.stacks) == 0 and len(tempdata) == 0:
                while stack.size() > self.toLimit:
                    t = stack.pop()
                    tempdata.append(t)
                self.stacks.append(stack)
            #if data leftover
                while len(tempdata) > 0:
                    newstack = Stack()
                    for i in tempdata[:self.toLimit]:
                        newstack.push(i)
                    self.stacks.append(newstack)
                    #RESET LIMIT self.toLimit + newstack.size() % self.limit
            #
    def pop(self):
        #need to deal with removing empty stacks
        if len(self.stacks) == 0: 
            return None
        else: 
            return self.stacks[-1].pop()
    def popAt(self, num):
        return self.stacks[num].pop()

stack1 = Stack()
stack2 = Stack()
data1 = [1,2,3,4,5,6,7]
data2 = [9,8,7,6,5,4,3,2,1]
for i in data1:
    stack1.push(i)
for i in data2:
    stack2.push(i)
print(stack1.size())
print(stack2.size())
print('----')
stackSet = SetOfStacks(8)
stackSet.push(stack1)
stackSet.push(stack2)
print(stackSet.toLimit)
