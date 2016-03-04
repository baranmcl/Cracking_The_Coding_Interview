'''
Given a sorted increasing order array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
'''
class tNode:
    def __init__(self, data=None, L=None, R=None):
        self.data = data
        self.L = L
        self.R = R

def sortedArraytoBSTRecursive(num, begin, end):
    if begin > end:
        return None
    midPoint = (begin+end) / 2
    root = tNode(num[midPoint])
    root.L = sortedArraytoBSTRecursive(num, begin, midPoint - 1)
    root.R = sortedArraytoBSTRecursive(num, midPoint+1, end)
    return root

def sortedArraytoBST(num):
    return sortedArraytoBSTRecursive(num, 0, len(num)-1)

array = [1,2,3,4,5,6,7,8,9]
myNode = sortedArraytoBST(array)
print(myNode.data)
print(myNode.L.data)
print(myNode.L.L.data)
print(myNode.L.R.data)
print(myNode.L.R.R.data)
print(myNode.R.data)
print(myNode.R.L.data)
print(myNode.R.R.data)
print(myNode.R.R.R.data)
