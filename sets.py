s1 = {'ab', 3,4, (5,6)}
s2 = {'ab', 7, (7,6)}
print(s1-s2)

# Returns all the items in both s1 and s2
print(s1.intersection(s2))

# Returns all the items in a set
print(s1.union(s2))

print('ab' in s1) # Testing for a member's presence in the set

# Lopping through elements in a set
for element in s1: 
    print(element)

# Frozen or Immutable sets
s1.add(frozenset(s2))
print(s1)

# Using frozen set as a key to a dictionary
fs1 = frozenset(s1)
fs2 = frozenset(s2)
{fs1: 'fs1', fs2: 'fs2'}



