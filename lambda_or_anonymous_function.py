# Lambda Or Anonymous Function is a way to write function in single line.

#Sorting Using Sort & Lambda Function

a=[[2,5],[1,2],[51,0]]
n=int(input("Enter Index of List 0 or 1 : "))
a.sort(key=lambda x:x[n])
print(a)


# multiply = lambda a,b:a*b
#
# # def multiply(a,b):
# #     return a * b
#
# a=int ( input ("Enter First Value : ") )
# b=int ( input ("Enter Second Value : ") )
# print("Multipication Is : ",multiply(a,b))