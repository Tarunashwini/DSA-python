class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
class Stacks:
    def __init__(self):
        self.head = None
        self.newnode = None
        self.prev  = None
    
    def push(self,data):
        
        if self.head == None:
            self.head  = Node(data)
            self.newnode = self.head
            self.prev = self.head
        else:
            self.newnode.right = Node(data)
            self.newnode = self.newnode.right
            self.newnode.left = self.prev
            self.prev = self.newnode
            
    def pop(self):
        self.prev = self.prev.left
        self.newnode = self.prev
        self.prev.right = None
        
    def display1(self):
        print("\nList from top to bottom.\n")
        cur = self.head
        
        while(cur is not None):
            print(cur.data, " >> ", end = " ")
            cur = cur.right
               
    
    
    def display2(self):
        print("\nList from bottom to top.\n")
        cur = self.prev
        
        while(cur is not None):
            print(cur.data, " >> ", end = " ")
            cur = cur.left
            
            

            
            
            
ll = Stacks()

n = int(input("Enter number of values:  "))

for i in range(n):
    data = int(input("Enter data : "))
    ll.push(data)
ll.display1()
ll.pop()
ll.pop()
ll.display2()
    
    
    
    
    
        
