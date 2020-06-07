
# Modifying behavior of an existing class through inheritance
class specialEmployee(Employee):
    def hours(self, numHours):
        self.own += numHours * self.rate * 2
        return("%.2f hours worked" % numHours)


