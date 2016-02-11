'''
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. 
The puzzle starts with disks sorted in ascending order of size from top to bottom
(i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks.
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
    def listItems(self):
        print(self.items)
        
def hanoi(n, source, helper, target):
    if n>0:
        # move tower of size n - 1 to helper
        hanoi(n-1, source, target, helper)
        # move from source peg to target
        if source:
            target.push(source.pop())
        # move tower of size n - 1 from helper to target
        hanoi(n-1, helper, source, target)
        
tower1 = Stack()
tower2 = Stack()
tower3 = Stack()
tower1.push(4)
tower1.push(3)
tower1.push(2)
tower1.push(1)
tower1.listItems()
tower2.listItems()
tower3.listItems()
print('---')
hanoi(tower1.size(), tower1, tower2, tower3)
tower1.listItems()
tower2.listItems()
tower3.listItems()
