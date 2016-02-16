'''
Implement a function to check if a linked list is a palindrome.
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
  def length(self):
    current = self.head_node
    length = 1
    while current:
        length += 1
        current = current.get_next()
    return length - 1

def isPalindrome(node, length):
    if length == 1: return True
    elif length == 2: return node.get_data() == node.get_next().get_data()
    else:
        current = node
        next_no = current.get_next()
        for i in xrange(length-1):
            current = current.get_next()
        if node.get_data() == current.get_data():
            return isPalindrome(next_no, length-2)
        return False

if __name__ == "__main__":
    linkeddata = [5,4,5,4,5,4]
    newList = LinkedList(Node(linkeddata[0]))
    for i in linkeddata[1:]:
        newList.insert(i)
    print(newList.displayList() == newList.displayList()[::-1])
    print(newList.length())
    print(isPalindrome(newList.head_node, newList.length()))
