'''
For the questions in this chapter, I'm going to be assuming the following for my linked list class.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class LinkedList: 
    def display(self,head):
        current = head
        while current:
            print(current.data)
            current = current.next
    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        current = head
        if current:
            while current.next != None:
                current = current.next
            current.next = new_node
            return head
        else:
            head = new_node
            return head
if __name__ == "__main__":
    mylist= LinkedList()
    T=[5,4,1,2,3]
    head=None
    for i in T:
        data=int(i)
        head=mylist.insert(head,data)    
    mylist.display(head); 	
