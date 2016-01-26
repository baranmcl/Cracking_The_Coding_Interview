'''
I'm going to implement an instance of a stack for testing in python.
LIFO!!!
'''
class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self, item):
    self.items.pop()
  def size(self):
    return len(self.items)

