'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer was not allowed?
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
  def display(self):
    current = self.head_node
    while current:
      print(current.get_data())
      current = current.get_next()
  def displayList(self):
    current = self.head_node
    result = []
    while current:
        result.append(current.get_data())
        current = current.get_next()
    return result
  def removeByData(self, data):
    current = self.head_node
    previous = None
    while current:
        if current.get_data() == data:
            if previous != None:
                previous.set_next(current.get_next())
                break
            else:
                current = current.get_next()
        previous = current
        current = current.get_next()
    
  def removeDups(self):
    dataHash = {}
    current = self.head_node
    while current:
        if current.get_data() not in dataHash:
            dataHash[current.get_data()] = 1
        elif current.get_data() in dataHash:
            dataHash[current.get_data()] += 1
        current = current.get_next()
    for key in dataHash:
        if dataHash[key] > 1:
            for i in range(dataHash[key]-1):
                self.removeByData(key)

if __name__ == "__main__":
    linkeddata = [5,4,1,2,3,4,6,5,2]
    newList = LinkedList(Node(linkeddata[0]))
    for i in linkeddata[1:]:
        newList.insert(i)
    print(newList.displayList())
    print(newList.removeDups())
    print(newList.displayList())
