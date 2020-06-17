# Named tuples returns a tuple like object that has fields accessible with named indexes

from collections import namedtuple

space = namedtuple('space', 'x y z')
sl = space(x = 2.0, y = 4.0, z = 10)
print(sl.x * sl.y * sl.z) # Calculating volume

space2 = namedtuple('space2', 'x def z', rename= True)
sl = space2(3,4,5)

print(sl._1)

sl = [4, 5, 6]
print(space._make(sl))

