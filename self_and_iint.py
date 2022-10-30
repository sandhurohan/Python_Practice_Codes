# Self & Init()
# Init() function is known as constructor. It is used to take input as argument.

# Class

class Workers:
    Company_Name="Tech Mahindra"

    def __init__(self,name,age,skill):
        self.name=name
        self.age=age
        self.skill=skill

    def printdetails(self):
        return f"Name : {self.name} Age : {self.age} Skill : {self.skill}"

    pass

worker1=Workers("Elon",21,"Painter")
worker2=Workers("Bhagwant Mann",45,"Member Of Parliament ")
worker3=Workers("Rajan",35,"Eye Specialist")
worker4=Workers("Sudhir",80,"Sweet Specialist")

print(worker1.printdetails())
print(worker2.printdetails())
print(worker3.printdetails())
print(worker4.printdetails())
