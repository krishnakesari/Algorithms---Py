from collections import OrderedDict
od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2

od2 = OrderedDict()
od2['two'] = 2
od2['one'] = 1

od1 = od2

print(od1)

