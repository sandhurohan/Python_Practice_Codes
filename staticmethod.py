# If we wanna to use object space

class Sections:
    def __init__(self,name,students):
        self.name=name
        self.students=students

    def printdetails(self):
        return f"Details are {name} {students}"

    @classmethod
    def from_slashes(cls,string):
        return cls(*string.split("/"))

    @staticmethod
    def printinput(string):
        print(f" Input is : {string}")

sec1=Sections.from_slashes("Red/54")
print(sec1.name)
print(sec1.students)

sec1.printinput("Input")

# # If we donot want to use object space
# @staticmethod
# def printstring(string):
#     print(f"Input is : {string}")
#
# printstring("rohan")