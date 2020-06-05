
# Recursive functions: tail iteration 

def iterTest(low,high):
    while low <= high:
        print(low)
        low = low+1

print(iterTest(1,4))

def recurTest(low,high):
    if low <= high:
        print(low)
        recurTest(low+1, high)

print(recurTest(1, 4))
