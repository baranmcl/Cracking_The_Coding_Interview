'''
Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes greater than or equal to x.
'''
class Node:
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node
  def set_next(self, node):
    self.next_node = node
  def get_next(self):
    return self.next_node
  def set_data(self, data):
    self.data = data
  def get_data(self):
    return self.data

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
    self.tail_node = head_node
  def insert(self, data):
    new_node = Node(data)
    if self.head_node == None:
        self.head_node = self.tail_node = new_node
    else:
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
  def removeNode(self, node):
      currentNode = node
      nextNode = node.get_next()
      currentNode.set_data(nextNode.get_data())
      currentNode.set_next(nextNode.get_next())
  def partitionList(self, data):
      current = self.head_node
      smaller = LinkedList()
      larger = LinkedList()
      while current:
          node_data = current.get_data()
          if node_data < data:
              smaller.insert(node_data)
          elif node_data >= data:
              larger.insert(node_data)
          current = current.get_next()
      smaller.tail_node.set_next(larger.head_node)
      return smaller
  def partitionList2(self, data, length):
      current = self.head_node
      prev = None
      for i in range(length):
          node_data = current.get_data()
          if node_data >= data:
              self.insert(node_data)
              nextNode = current.get_next()
              if current == self.head_node:
                  self.head_node = nextNode
                  current = nextNode
              else: 
                  prev.set_next(nextNode)
                  current = nextNode
          else:
              prev = current
              current = current.get_next()
      return self
    
  def size(self):
      current = self.head_node
      count = 0
      while current:
          count += 1
          current = current.get_next()
      return count


if __name__ == "__main__":
    linkeddata = [5,4,1,2,3,4,6,5,2]
    newList = LinkedList(Node(linkeddata[0]))
    for i in linkeddata[1:]:
        newList.insert(i)
    print(newList.displayList())
#    newList = newList.partitionList(3)
    newList = newList.partitionList2(3, newList.size())
    print(newList.displayList())
