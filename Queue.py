
# Listing queue
class ListQueue:
    def __int__(self):
        self.items = []
        self.size = 0

# Enqueue operation
## Inserts an object in front of the list
def enqueue(self, data):
    self.items.insert(0, data)
    self.size += 1

# Dequeue Operation
## removes last item from the queue
def dequeue(self):
    data = self.items.pop()
    self.size -= 1
    return data

# Stack based queue
class Queue:
    def __init__(self):
        self.inbound_stack = []  # to store elements added to the queue
        self.outbound_stack = []

# Enquue Operation
def enqueue(self, data):
    self.inbound_stack.append(data)

queue = Queue()
queue.enqueue(5)
print(queue.inbound_stack)