# Public
class Employee:
    def __init__(self,name):
        self.name=name  #Public

# Public

class Employee1:
    def __init__(self,name):
        self._name=name  #Protected

#Protected
class Employee2:
    def __init__(self,name):
        self.__name=name  #Private

