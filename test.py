
num = [1,2,3]

for x in num:
    x = int(x*x/2)
    print(x)

num = [22,35,68]

for x in num:
    if x == 22:
        print("One")
    elif x == 35:
        print("two")
    elif x == 6:
        print("three")
    else:
        print("None")


def main():
    num2 = [x * x for x in num]
    print2(num2)

def print2(a):
    for x in a: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


def main():
    num3 = [int(x*x/2) for x in num]
    print3(num3)

def print3(a):
    for x in a: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


## Defining an algebraic function

def main():
    binomial = [(2*num[0] + 3*num[1]) for x in num]
    printb(binomial)

def printb(c):
    for x in c : print(x, end = ' ')
    print()

if __name__ == '__main__': main()

## Defining algebraic expression 2

def main():
    x = 3 * num[0]
    y = 4 * num[1]
    add_binomial = [x + y for a in num]
    printc(add_binomial)

def printc(o):
    for a in o: print(a, end = ' ')
    print()

if __name__ == '__main__': main()
















