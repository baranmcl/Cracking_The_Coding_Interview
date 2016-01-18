'''
the file in which I attempt to code a linkedlist instance to mess around with.
'''
class Node:
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node
  def set_next(self, node):
    self.next_node = node
  def get_next(self):
    return self.next_node
  def get_data(self):
    return self.data

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  def displayList(self, head_node):
    current = head_node
    while current:
      print(current.get_data())
      current = current.get_next()
