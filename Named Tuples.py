from collections import namedtuple

space = namedtuple('space', 'x y z')
s1 = space(x = 2.0, y = 4.0, z = 10)
print(s1.x * s1.y * s1.z) # Calculating volume