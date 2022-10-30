#------------------------------ MAP ----------------------------------------------

# Map Function is used to apply single function to whole list. Can be More Clearified from Example Listed Below
# Map Function Give us Index Number called MAP Index, we need to typecaste that Index to LIST to make it readable

# If we want to typecaste string list to INT list

# list1=["1","2","3","4","5","6"]
# list1=list(map(int,list1))

# def square(n):
#     return n*n
#
# list2=[1,2,3,4,5,6,7,8,9,10]
# print(list2)
# sqlist=list(map(square,list2))
# print(sqlist)
#
# list3=[1,2,3,4,5,6,7,8,9]
# print(list3)
# sqlist=list(map(lambda n:n*n,list3))
# print(sqlist)
#
# def square(n):
#     return n*n
#
# def cube(n):
#     return n*n*n
#
# list5=[square,cube]
#
# for i in range(1,6):
#     ans=list(map(lambda x:x(i),list5))
#     print(ans)


#------------------------------ FILTER -------------------------------------------

# Filter Function is used to filter list
# Like Here we want list of number smaller than 67

# list6=[45,64,48,346,271,1,5,4,8,244,52]
#
# def issmaller(n):
#     return n<65
#
# small_list=list(filter(issmaller,list6))
# print(small_list)


# ------------------------------ REDUCE -------------------------------------------

# Reduce is part of functool. It is used to reduce length of code.
# If we want to print sum of list.

# from functools import reduce
#
# list7=[1,2,3,4,5,6,7,8,9,55]

# ------------------------------- Ordinary Way ------------------------------------

# num=0
# for i in list7:
#     num=num+i
# print(num)

# --------------------------------  REDUCE WAY ----------------------------------------
#
# sum=reduce(lambda x,y:x+y,list7)
# print(sum)