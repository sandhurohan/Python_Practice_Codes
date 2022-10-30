#Typecasting Matrix
def cast_matrix(lP, data_type):
    return list(map(lambda sub: list(map(data_type, sub)), lP))

T=int(input())

lP = []
lN = []
for i in range(0,T):
    NP = input()
    np1 = NP.split()

    for j in range(0,int(np1[0])):
        x=input()
        y=x.split()
        y.sort()
        lP.append(y)
    res_matrix = cast_matrix(lP, int)
    lN.append(res_matrix)
    lP=[]

print(lN)








# N=int(input())
# l=[]
# l2=[]
# for i in range(0,N-1):
#     k=input()
#     sp=k.split()
#     l2.append(int(sp[0]))
# count1=0
# for j in range(1,N):
#     count1=l2.count(j)
#     l.append(count1)
#     count1=0
# print(l)
# mul=1
# for i in range(0,len(l)):
#     if l[i]>0:
#         mul=mul*l[i]
# print(mul)
#
# fact = 1
#
# for i in range(1, mul + 1):
#     fact = fact * i
# print(fact)