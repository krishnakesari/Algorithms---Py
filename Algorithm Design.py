
# Divide and conquer - Power of smaller subgroups
# Greedy Algorithms - Optimization and combinatorial problems
## 1. Travelling salesman problem - closest destination first
# Dynamic Programming - when sub problems overlap

# Recursion and Backtracking (Divide and Conquer)
## Base cases - Tells when to terminate (eg: n = 0)
## Recursive cases - Calls functions (Eg: n > 0)

def factorial(n):
        #test for a base case
        if n==0:
            return 1
            # make a calculation and a recursive call
            f= n*factorial(n-1)
        print(f)
        return(f)
        factorial(4)

def sum(n):
    if n > 0:
        f = n + 1
        print(f"If n = {n}, the value of f is {f}")

sum(6)

# Back Tracking (Divide and Conquer)
## Traversing tree structure, if needed we can backtrack to previous node and traverse a different branch

def bitStr(n,s):
    if n == 1 : return s
    # Generate all possible permutations of a given string
    return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]

print(bitStr(3,'abc'))

# Karatsuba Algorithm (Long Multiplication)
## Steps
## 1. Build a recursive algorithm
## 2. Split into two halves (first half most significant digits, second half least significant digits)

from math import log10

def karatsuba(x,y): 

    # The base case for recursion 
    if x < 10 or y < 10: 
        return x*y     

    #sets n, the number of digits in the highest input number 
    n = max(int(log10(x)+1), int(log10(y)+1)) 

    # rounds up n/2     
    n_2 = int(math.ceil(n / 2.0)) 
    #adds 1 if n is uneven 
    n = n if n % 2 == 0 else n + 1 

    #splits the input numbers      
    a, b = divmod(x, 10**n_2) 
    c, d = divmod(y, 10**n_2) 

    #applies the three recursive steps 
    ac = karatsuba(a,c) 
    bd = karatsuba(b,d) 
    ad_bc = karatsuba((a+b),(c+d)) - ac - bd 

    #performs the multiplication     
    return (((10**n)*ac) + bd + ((10**n_2)*(ad_bc))) 

print(karatsuba(15,14))

















