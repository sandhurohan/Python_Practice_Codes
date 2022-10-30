N=int(input("Enter Amount Of Elements To Be Entered In List : "))
l=[]
for i in range(0,N):
    x=int(input())
    l.append(x)

for i in range(0,N):
    if l[i]<10:
        pass
    else:
        m=l[i]
        while True:
            m=int(m)+1
            m=str(m)
            if m==m[::-1]:
                l[i]=m
                break
print(l)