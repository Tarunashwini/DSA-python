class Node:
    def __init__ (self,data):
        self.data = data
        self.next_ = None
        
class linkedlist:
    def __init__ (self):
        self.head = None
        self.lastnode = None
        
    def appenddata(self, data):
        
        if self.head == None:
            self.head = Node(data)
            self.lastnode = self.head
        else:
            self.lastnode.next_ = Node(data)
            self.lastnode = self.lastnode.next_
    
    
    def display(self):
        curr = self.head
        
        while curr is not None:
            print(curr.data," >> ", end = "")
            curr = curr.next_
            
    
list_ = linkedlist()
n = int(input("enter n :  "))

for i in range(0,n):
    data = int(input("Enter the data of : "))
    list_.appenddata(data)

print("linkedlist :::   ")
list_.display()
    
    
    
    
