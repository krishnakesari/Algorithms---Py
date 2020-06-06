# Classes - a set of attributest that are shared across instances of that class.
## 1. Number of methods
## 2. Class variables
## 3. Computed properties

## Functions are defined inside a class called "instance methods"

class Employee(object): 
    numEmployee = 0  # Counting number of employee instances
    def __init__(self, name, rate): 
        self.owed = 0         
        self.name = name 
        self.rate=rate 
        Employee.numEmployee += 1 

    def __del__(self): 
        Employee.numEmployee -= 1 

    def hours(self, numHours): 
        self.owed += numHours * self.rate 
        return("%.2f hours worked" % numHours) 

    def pay(self):                 
        self.owed = 0 
        return("payed %s " % self.name) 

emp1 = Employee("Jill", 18.50)
emp2 = Employee("Jack", 15.50)

print(Employee.numEmployee)

print(emp1.hours(20))
print(emp1.owed)
print(emp1.pay)