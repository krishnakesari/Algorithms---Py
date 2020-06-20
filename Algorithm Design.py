
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

def factorial(n):
    if n > 2:
        print(n)

factorial(6)