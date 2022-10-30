# #Fibonacci
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
#
# n=int(input("Enter then number : "))
# while n!=0:
#     print(fibonacci(n),end=" ")
#     n=n-1

#Factorial Using Itrative Approach

# def factorial(n):
#     fac=1
#     for i in range(1,n):
#         fac=fac*(i+1)
#     return fac
#
# n=int(input("Enter Any Number : "))
# print("Factorial Is ",factorial(n))

#Factoraial Using Recursive approach

# def factorail2(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorail2(n-1)
#
# n=int(input("Enter Any Number : "))
# print("Factorial Is : ",factorail2(n))
