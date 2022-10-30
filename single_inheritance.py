
# In OOPS INHERITANCE means copying the already built class & using its functions by adding more functions to it.

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def printdetails(self):
        return f"Name is {self.name}, Age is {self.age} & Job is {self.salary} "

    @classmethod
    def splitstring(cls,str):
        return cls(*str.split("/"))

# Single Inheritance Class

class Programmers(Employee):

    def printprog(self):
        return f"Name is {self.name} Age is {self.age} Job is {self.salary}"

e1=Employee.splitstring("Raman/20/Trainer")
e2=Programmers.splitstring("Rajat/24/Milkman")

print(e2.printprog())
# print(e1.name)
# print(e2.name)
