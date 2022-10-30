# def fun1(a,b,c,d):
#     print(a,b,c,d)

def funargs(normal,*args,**dict):

    print(normal)
    print()
    
    for items in args:
        print(items)

    print()

    for key,values in dict.items():
        print(f"{key} Costs {values}")

# def funargs1(*args):
#     for items in args:
#         print(items)

# a=input("Enter Name : ")
# b=input("Enter Name : ")
# c=input("Enter Name : ")
# d=input("Enter Name : ")

# fun1(a,b,c,d)
normal="I am Normal Text"
list=["Apple","Mango","Banana","Grapes"]
dict={"Apple":"5$","Mango":"6$","Banana":"7$","Grapes":"4$"}
# list1=["Apple1","Mango1","Banana1","Grapes1"]

funargs(normal,*list,**dict)
# funargs1(*list1)

# This will pass list as tuple  to function funargs