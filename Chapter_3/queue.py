'''
I'm going to implement a queue data structure for me to mess around with.
FIFO!
'''
class Queue:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self, item):
    self.items.pop(0)
  def size(self):
    return len(self.items)
