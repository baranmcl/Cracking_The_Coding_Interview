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
    self.tail_node = head_node
  def insert(self, data):
    new_node = Node(data)
    self.tail_node.set_next(new_node)
    self.tail_node = new_node
  def displayList(self):
    current = self.head_node
    while current:
      print(current.get_data())
      current = current.get_next()
      
      
linkeddata = [5,4,1,2,3]
newList = LinkedList(Node(linkeddata[0]))
for i in linkeddata[1:]:
    newList.insert(i)
newList.displayList()
