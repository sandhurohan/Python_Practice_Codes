# For HIgher Versions
# For Lower Versions Of Python

from abc import ABC,abstractmethod
class Shapes(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shapes):
    shape="Rectangle"
    sides=4

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def printarea(self):
        return self.length*self.breadth

rect1=Rectangle(12,45)
print(rect1.printarea())
# # For Lower Versions Of Python
#
# from abc import ABCMeta,abstractmethod
# class Shapes(metaclass=ABCMeta):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shapes):
#     shape="Rectangle"
#     sides=4
#
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#
#     def printarea(self):
#         return self.length*self.breadth
#
# rect1=Rectangle(12,45)
# print(rect1.printarea())
