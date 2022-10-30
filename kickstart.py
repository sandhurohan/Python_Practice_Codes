n=int(input())
l=[]
for i in range(0,n):
    x=input()
    l.append(x)

# print(l[0][1])
y=0
for i in range(0,n):
    for j in range(0,len(l[i])):
        y+=int(l[i][j])


z=-1
for i in range(0,10):
    if (y+i)%9==0:
        z=i
print(z)

lf=[]
lf1=[]
# for o in range(0,n):
for i in range(0,n):
    for j in range(0,len(l[i])):
        k=l[i][:j]+str(z)+l[i][j:len(l[i])+1]
        lf.append(int(k))
    side=l[i]+str(z)
    lf.append(int(side))
    lf.sort()
    lf1.append(lf)
    lf=[]

lf1.sort()
print(lf1)

#
# for j in range(int(input())):
#     n = int(input())
#
#
#     def digSum(n):
#
#         if (n == 0):
#             return 0
#         if (n % 9 == 0):
#             return 9
#         else:
#             return (n % 9)
#
#
#     x = 9 - digSum(n)
#     s = str(n)
#     ans = s + str(x)
#     for i in range(0, len(s)):
#         temp = s[0:i] + str(x) + s[i:len(s)]
#         if (temp[0] == '0'):
#             continue
#         ans = min(temp, ans)
#     print("Case #", j + 1, ": ", ans, sep="")