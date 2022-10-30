T=int(input())
for j in range(0,T):
    N=int(input())
    G=int(input())
    l1=[]
    for i in range(0,G):
        x=input()
        l1.append(x)
    l1.sort()
    y=0
    for i in range(0,N):
       y=y+int(l1[i])
    print(y)
