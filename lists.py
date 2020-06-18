# Creating  a list

x = 1; y = 2; z = 3
list1 = [x,y,z]

list2 = list1
list2[1] = 4

print(list1)

# Creating expression from list (list comprehensions)
l = [2,4,8,16]
print([i ** 3 for i in l])

# Creating composite functions

items = [["rice", 2.4, 8], ["flour", 1.9, 5], ["corn", 4.7, 6]]
for item in items:
    print("Product: %s Price: %.2f Quality: %i" % (item[0], item[1], item[2]))

# Bracket Operations
items[1][1] = items[1][1] * 1.2
print(items[1][1])

# list comprehension
def f1(x): return x*2 
def f2(x): return x*4 

lst = [] 
for i in range(16): 
    lst.append(f1(f2(i))) 
print(lst) 
print([f1(x)  for x in range(64) if x in [f2(j) for j in range(16)]]) 

# Multiplying elements in a list with each other
list1 = [[1,2,3], [4,5,6]]
print([i * j for i in list1[0] for j in list1[1]])

# Splitting sentence with complex functions
words = 'here is a sentence'.split()
print([[word, len(word)] for word in words])

## Testing lists
l = [1,2,3,4]
print(l)