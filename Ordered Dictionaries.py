from collections import OrderedDict
od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2

od2 = OrderedDict()
od2['two'] = 2
od2['one'] = 1

print(od1 == od2)
print(od1)

# Creating an order list

kvs = [('three',3), ('four', 4), ('five',5), ('six',6)]
od1.update(kvs)
print(od1)

for k, v in od1.items():
    print(k,v)

# Using Lambda functions
od3 = OrderedDict(sorted(od1.items(), key = lambda t : (4*t[1]) - t[1]**2))

print(od3.values())

