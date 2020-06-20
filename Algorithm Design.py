
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