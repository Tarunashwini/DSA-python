#Creation of a Binary Tree using python

class Node:
    def __init__ (self, data):
        self.left = None
        self.data = data
        self.right = None
        
        
    def insert(self,data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                
            if data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()

