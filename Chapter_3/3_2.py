'''
How would you design a stack which , in addition to push and pop, also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
'''
class Stack2:
  def __init__(self):
    self.items = []
    self.minimum = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
    if not self.minimum or item <= self.min():
        self.minimum.append(item)
  def pop(self, item):
    x = self.items.pop()
    if x == self.min():
        self.minimum.pop()
    return x
  def size(self):
    return len(self.items)
  def min(self):
    return self.minimum[-1]
