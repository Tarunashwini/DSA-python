## Doubly Linked Lists

class Node:
    def __init__ (self, data):
        self.left = None
        self.data = data
        self.right = None
        
class DoubleList:
    def __init__ (self):
        self.head = None
        self.newnode = None
        self.lastnode = None
    
    def insert(self,data):
        if self.head is None:
            self.head = self.newnode = self.lastnode = Node(data)
        else:
            self.newnode.right = Node(data)
            self.newnode = self.newnode.right
            self.newnode.left = self.lastnode
            self.lastnode  = self.newnode
            
    def Straignt_Display(self):
        cur = self.head
        
        print("Displaying the list in forward direction :   ")
        
        while(cur is not None):
            print(cur.data, ">>> ", end = " ")
            cur = cur.right
            
            
    def reverse_display(self):
        cur = self.newnode
        print()
        print("Displaying the list in reversed direction :   ")
        
        while(cur != self.head):
            print(cur.data, "<<< ", end = " ")
            cur = cur.left
            
        print(cur.data)
            
llist = DoubleList()
n = int(input("Enter number of values :   "))

for i in range(n):
    data = int(input("Enter the values:    "))
    llist.insert(data)
    
llist.Straignt_Display()
llist.reverse_display()
    
