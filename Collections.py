
# Deques
## Double ended queues - list like objects that support thread-safe, meomory efficient appends

from collections import deque

dq = deque('abc')
dq.append('d') # add value to the right
dq.appendleft('z') # add value to the left
dq.extend('efg') # add multiple items to the right
dq.extendleft('ywx') # add multiple items to the left
print(dq)

# using pop and popleft()
dq.pop() # returns and removes an item from the right
dq.popleft() # returns and removes an items from left
print(dq)

# Rotate all items two steps to the right
dq.rotate(2)
print(dq)
# Rotate all items two steps to the left
dq.rotate(-2)
print(dq)

# Slicing a deque
# list(itertools.islice(dq,3,9))

# Circular Buffer - to generate fixed size structure
dq2=deque([],maxlen=3) 
for i in range(6): 
    dq2.append(i) 
    print(dq2) 
