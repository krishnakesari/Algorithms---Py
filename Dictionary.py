d ={'one': 1 , 'two': 2, 'three': 3 } # creates a dictionary 
d.update({'five': 5, 'six': 6}) #add multiple items 

print(d)
print('five' in d)


# Sorted dictionaries
print(sorted(list(d))) # Alphabetical order
print(sorted(d.values())) # Ascending order

# Sorting according to the value
print(sorted(list(d), key = d.__getitem__))

# Key value pair based sorting
print([value for (key, value) in sorted(d.items())])

# Sorting in reverse order
print(sorted(list(d), key = d.__getitem__, reverse = True))

d2 ={'one':'uno' , 'two':'deux', 'three':'trois', 'five': 'cinq', 'six':'six'}
print(d2)

# Sorting dictionary using other dictionary
print(sorted(d2, key=d.__getitem__))

# Use a list comprehension to sort values of the french to English dictionary
print([d2[i] for i in sorted(d2, key = d.__getitem__)])

# Defining a custom sort

def corder(string):
    return(string[len(string)-1])

print(sorted(d2.values(), key=corder))