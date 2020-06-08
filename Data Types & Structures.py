# Operations and expressions
# 1. None Type - immutable - often used as a default value in optional arguments to allow functions to detect whether the caller passed a value.

# 2. Boolean
## a. not x (Returns True if x is false otherwise)
## b. x and y (Return True if x and y are true)
## c. x or y

# 3. Integer, float, or complex zero
# 4. Empty sequence or mapping
# 5. User defined classes __len__() or __bool__()

# Comparision and Arithmetic Operators
## + - * /  // quotient (3 // 2 returns 1)
## x ** y (exponent)
## x % y (remainder)
## < <= > >= == !=


# Membership, identity and logical operations
x = [1,2,3];  y = [1,2,3]
print(x == y) # Equivalence
print(x is y)  # Object Identity
x = y  # Assignment
print(x is y) 

# Representation Error
print(1-0.9)
print(1-0.9 == 0.1)

# Precision / Rounding
import decimal
x = decimal.Decimal(3.14);
y = decimal.Decimal(2.74)
print(x * y)
decimal.getcontext().prec = 4 # Precision 
print(x * y)

# Handling Fractions
import fractions
print(fractions.Fraction(3,4))
print(fractions.Fraction(0.5))
print(fractions.Fraction("0.25"))

# Sequences
## Ordered sets of objects indexed by non-negative integers
## List and Tuples - sequences of arbitrary objects
print(tuple('sequence'))
## strings - sequences of characters
## string, tuple and range objects are immutable (only return a value rather than actually change the value)

## len(s) - number of elements
## min, max, sum, all, any 
## s + r, s * n,
## s[i] - Indexing returns elements i of s
## s[i:j:stride] - Slicing returns elements between i and j with optional stride
##  x in s (Returns True if element x is in s), x not in s

l = ['one', 'two']
x, y = l
x, y = y, x
print(y,x)


