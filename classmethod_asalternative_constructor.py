class Employee:
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age

    def printdetails(self):
        return f" Details are {self.name}{self.salary}{self.age}"

    @classmethod
    def from_slash(cls,string):
        # param=string.split("/")
        # print(param)
        # return cls(param[0],param[1],param[2])
        return cls(*string.split("/"))

emp1=Employee.from_slash("Karan/48000/21")
print(emp1.age)