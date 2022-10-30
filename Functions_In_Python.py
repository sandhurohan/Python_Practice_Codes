"""def fun1():
    print("You are in fun1()")

fun1()
"""
a=int(input("Enter Value of A "))
b=int(input("Enter Value of b "))
def fun2(a,b):
    c=a+b
    return c

print("The Addition of A & B is",fun2(a,b))

#Docstring
a=int(input("Enter Value of A "))
b=int(input("Enter Value of b "))
def fun3(a,b):
    """I will Add 2 Numbers"""
    c=a+b
    return c

print(fun3.__doc__)