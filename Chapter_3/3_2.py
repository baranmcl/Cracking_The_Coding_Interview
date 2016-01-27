'''
How would you design a stack which , in addition to push and pop, also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
'''
class Stack2:
  def __init__(self):
    self.items = []
    self.minimum = self.prevMin = None
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
    if self.minimum == None:
      self.minimum = item
    elif self.minimum > item:
      self.prevMin = self.minimum
      self.minimum = item
  def pop(self, item):
    self.items.pop()
    if item == self.minimum:
      self.minimum = self.prevMin
    ### needs more code here. What if pop is done twice? prevMin needs to go back further
  def size(self):
    return len(self.items)
  def min(self):
    return self.minimum
