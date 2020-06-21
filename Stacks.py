# Basic stack
def b(): 
    print('b') 

def a(): 
    b() 

a() 
print("done") 

# Stack Implementation
## Creating node class
class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class Stack: 
    def __init__(self): 
        self.top = None 
        self.size = 0 

# Push Operation
def push(self, data): 
       node = Node(data) 
       if self.top: 
           node.next = self.top 
           self.top = node                 
       else: 
           self.top = node 
       self.size += 1 

# POP Operation
def pop(self): 
        if self.top: 
            data = self.top.data 
            self.size -= 1  
            if self.top.next: 
                self.top = self.top.next 
            else: 
                self.top = None 
            return data 
        else: 
            return None

# Peek Operation

def peek(self):
    if self.top:
        return self.top.data
    else:
        return None

