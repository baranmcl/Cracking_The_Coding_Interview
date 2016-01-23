'''
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
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
  def removeNode(self, node):
      currentNode = node
      nextNode = node.get_next()
      currentNode.set_data(nextNode.get_data())
      currentNode.set_next(nextNode.get_next())
def addTwo(L1, L2):
    if L1 == None:
        return L2
    if L2 == None:
        return L1
    head = current1 = L1.head_node
    current2 = L2.head_node
    carry = (current1.get_data() + current2.get_data()) / 10
    head.set_data((current1.get_data() + current2.get_data()) %10)
    while current1.get_next() != None and current2.get_next() != None:
        carry += current1.get_next().get_data()
        carry += current2.get_next().get_data()
        current1.get_next().set_data(carry % 10)
        carry = carry // 10
        current1 = current1.get_next()
        current2 = current2.get_next()
    if current1.get_next() == None:
        current1.set_next(current2.get_next())
    while current1.get_next() != None:
        carry += current1.get_next().get_data()
        current1.get_next().set_data(carry % 10)
        carry = carry // 10
        current1 = current1.get_next()
    if carry > 0:
        current1.set_next(Node(carry))

if __name__ == "__main__":
    number1 = LinkedList(Node(7))
    number1.insert(1)
    number1.insert(6)
    number2 = LinkedList(Node(5))
    number2.insert(9)
    number2.insert(2)
    print(number1.displayList())
    addTwo(number1, number2)
    print(number1.displayList())
