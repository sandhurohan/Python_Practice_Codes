# Diamond Shape Problem is multiple inheritance problem in which compiler get confused
# that whom's method will get implemented & whom's not.

# Thats Why Java Does'nt support Multiple Inheritance
# It creates lot of problem in C++ while in Python everything is crystal clear.

class A():
    def func1(self):
        print(" U are In Function [A]")


class B(A):
    # def func1(self):
    #     print(" U are In Function [B]")
    pass

class C(A):
    # def func1(self):
    #     print(" U are In Function [C]")
    pass

class D(B,C):
    pass
    # def func1(self):
    #     print(" U are In Function [D]")

a=A()
b=B()
c=C()
d=D()

d.func1()