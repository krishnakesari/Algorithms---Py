## dir(object) gives list of attributes of a particular object
## Begin and end with two underscore (__) is a special method
## __init__ method, invokes initializer of super class in our own class definitions

class my_class(): 
    def __init__(self, greet): 
        self.greet = greet 
    def __repr__(self):   # a string representation of our object
        return 'a custom object (%r)' % (self.greet) 

a = my_class('giday')
print(a)

