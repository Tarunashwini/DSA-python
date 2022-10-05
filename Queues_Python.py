class Node:
    def __init__(self,data):
        self.data = data
        self.next_= None
        
class Queues:
    def __init__(self):
        self.head = self.tail=self.cur = None
    
    def insert(self,data):
        if (self.head == None):
            self.head = self.tail=self.cur = Node(data)
            
        else:
            self.head.next_ = Node(data)
            self.head = self.head.next_
    def remove(self):
        cur = self.tail.next_
        self.tail.next_ = None
        self.tail = cur
        
    def Display(self):
        cur = self.tail
        while(cur):
            print(cur.data," >> ",end="")
            cur = cur.next_
            
ll = Queues()

n = int(input("Enter the data:    "))

for i in range(n):
    data = int(input("Enter the data:   "))
    ll.insert(data)


print("Queue before removing.")

ll.Display()
ll.remove()
ll.remove()

print("\nQueue after removing.")

ll.Display()
            
            
            
            
            
