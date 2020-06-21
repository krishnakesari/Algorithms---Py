# dequeue Operation
if not self.outbound_stack: 
    while self.inbound_stack: 
        self.outbound_stack.append(self.inbound_stack.pop()) 
return self.outbound_stack.pop() 


queue = Queue() 
queue.enqueue(5) 
queue.enqueue(6) 
queue.enqueue(7) 
print(queue.inbound_stack) 
queue.dequeue() 
print(queue.inbound_stack) 
print(queue.outbound_stack) 
queue.dequeue() 
print(queue.outbound_stack) 
