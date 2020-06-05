
# High Order Functions:

## map() - to transform each item into an iterable object
lst = [1,2,3,4]
print(list(map(lambda x:x**3, lst)))

## filter() - To filter items in a list

lst2 = list(filter((lambda x: x<3), lst))
print(lst2)

### Passing words len function to sort function
words = str.split('The longest word in this sentence')
print(sorted(words, key = len))

# Sort in alphabetical orfer with lower comes after capital letter
sl = ['A', 'b', 'a', 'C', 'c']
sl.sort(key=str.lower)
print(sl)

# Simple sort
sl = ['A', 'b', 'a', 'C', 'c']
s2 = sl.sort()
print(s2)

### Sorting based on item
items = [["rice", 2.4,8], ["flour", 1.9,5], ["Corn", 4.7,6]]
items.sort(key=lambda item: item[1])
print(items)

