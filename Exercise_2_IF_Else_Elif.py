#FaultyCalculator
#45*3=55,56+9=77,56/6=4
print("Enter First Value : ")
a=int(input())
print("Enter Second Value : ")
b=int(input())
print("Press 1 : Add, 2 : Subtract, 3 : Multiply, 4 : Division, 5 : Remainder")
opt=int(input())
if opt==1:
    if a==56 and b==9:
        print("77")
    else:
        print(a+b)
elif opt==2:
        print(a-b)
elif opt==3:
    if a==45 and b==3:
        print("5455")
    else:
        print(a*b)
elif opt==4:
    if a==5 and b==6:
        print("4")
    else:
        print(a/b)
elif opt==5:
    print(a%b)
else :
    print("Invalid Option")