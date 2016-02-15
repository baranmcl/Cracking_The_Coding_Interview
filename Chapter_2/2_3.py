'''
Implement an algorithm to delete a node in the middle of a singly-linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a-> b-> c-> d-> e
Result: Nothing is returned, but the new linked list looks like a-> b-> d-> e
'''
class Node:
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node
    
  @property
  def next_n(self):
    return self.next_node    
  @next_n.setter
  def next_n(self, node):
    self.next_node = node
  
  @property  
  def _data(self):
    return self.data
  @_data.setter
  def _data(self, data):
    self.data = data

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
    self.tail_node = head_node
  def insert(self, data):
    new_node = Node(data)
    self.tail_node.next_n = new_node
    self.tail_node = new_node
  def display(self):
    current = self.head_node
    while current:
      print(current._data)
      current = current.next_n
  def displayList(self):
    current = self.head_node
    result = []
    while current:
        result.append(current._data)
        current = current.next_n
    return result
  def displayList2(self):
    current = self.head_node
    result = []
    while current:
        if current._data == 3:
            self.removeNode(current)
        else:
            result.append(current._data)
            current = current.next_n
    return result
  def removeByData(self, data):
    current = self.head_node
    previous = None
    while current:
        if current._data == data:
            if previous != None:
                previous.next_n = current.next_n
                break
            else:
                current = current.next_n
        previous = current
        current = current.next_n
  def removeNode(self, node):
      currentNode = node
      nextNode = node.next_n
      currentNode._data = nextNode._data
      currentNode.next_n = nextNode.next_n

if __name__ == "__main__":
    linkeddata = [5,4,1,2,3,4,6,5,2]
    newList = LinkedList(Node(linkeddata[0]))
    for i in linkeddata[1:]:
        newList.insert(i)
    print(newList.displayList())
    print(newList.displayList2())
