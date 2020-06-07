
# Modifying behavior of an existing class through inheritance
class specialEmployee(Employee):
    def hours(self, numHours):
        self.own += numHours * self.rate * 2
        return("%.2f hours worked" % numHours)

## For a sub-class to define a new class vairable, it needs __init__() method:
class specialEmployee(Employee): 
    def __init__(self,name,rate, bonus): 
        Employee.__init__(self, name, rate) #calls the base classes 
        self.bonus = bonus 

    def hours(self, numHours): 
        self.owed += numHours * self.rate + self.bonus  
        return("%.2f hours worked" % numHours)  

    
class Aexp(object): 
    base=2 
    @classmethod 
    def exp(cls,x): 
        return(cls.base**x) 

class Bexp(Aexp): 
    base=3 

BxSqr.sqr(3)