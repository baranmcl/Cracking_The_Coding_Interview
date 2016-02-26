'''
Implement a functino to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree 
such that the heights of the two subtrees of any node never differ by more than one. 
'''
class tNode:
    def __init__(self, data=None, L=None, R=None):
        self.data = data
        self.L = L
        self.R = R
    def set_data(self, data):
        self.data = data
    def set_L(self, L):
        self.L = L
    def set_R(self, R):
        self.R = R
    def get_data(self):
        return self.data
    def get_L(self):
        return self.L
    def get_R(self):
        return self.R
class bTree:
    def __init__(self, head=None):
        self.head = head
    def isBalanced(self, current):
        shortestDepth = None
        longestDepth = None
        
        if abs(shortestDepth - longestDepth) > 1: return False


level3A = tNode(8)
level2D = tNode(7)
level2C = tNode(6)        
level2A = tNode(5, level3A)
level2B = tNode(4)        
level1B = tNode(3, level2C, level2D)
level1A = tNode(2, level2A, level2B)
head = tNode(1)
