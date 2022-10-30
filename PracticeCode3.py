n=int(input("Enter No. of Elements : "))
l=[]

for i in range(0,n):
    x=int(input())
    l.append(x)

l1=l.copy()
l2=l.copy()

l.reverse()
print(l)

a2=l1[::-1]
print(a2)

y=int(len(l2)/2)
j=len(l2)-1

# // is used to return integer input

for i in range(len(l2)//2):
    l2[i],l2[len(l2)-1-i]=l2[len(l2)-1-i],l2[i]

print(l2)

if l==a2 and a2==l2:
    print("All Same!!")
else:
    print("Different")
