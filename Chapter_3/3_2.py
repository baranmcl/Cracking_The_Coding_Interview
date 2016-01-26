'''
How would you design a stack which , in addition to push and pop, also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
'''
class Stack:
  def __init__(self):
    self.items = []
    self.minimum = min(self.items)
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self, item):
    self.items.pop()
  def size(self):
    return len(self.items)
