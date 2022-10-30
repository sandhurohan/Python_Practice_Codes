# n=int(input("Enter Number Of Rows : "))
#
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print()

n=int(input("Enter Number Of Rows : "))
b=int(input("Enter Boolean Value ( 0 or 1 ) : "))

if b==0:
    print()
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print()

elif b==1:
    print()
    for i in range(0,n):
        for j in range(i,n):
            print("* ",end="")
        print()
