class A():
    classvar1="I am Class [A] Variable"

    # Constructor
    def __init__(self):
        self.var1="I am Constructor Variable Of Class [A]"
        self.classvar1="I am instance variable in Class [A]"
class B(A):
    classvar2 = "I am Class [B] Variable"
    def __init__(self):
        self.var1 = "I am Constructor Variable Of Class [B]"
        self.classvar1 = "I am instance variable in Class [B]"
        super().__init__()

a=A()
b=B()
print(b.classvar1)