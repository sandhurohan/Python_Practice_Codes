# Pendulem Code
N=int(input())
S1=input()
l=input()
l1=S1.split()
f=int(l1[0])
l2=l.split()
j=0
ans=[]
for i in range(0,N):
   j=j+int(l2[i])
   ans.append(j)
if f in ans:
    print("Possible")
else:
    print("Not Possible")

# import random
# t=int(input())
#
# if __name__ == '__main__':
#     for i in range(0,t):
#         my_string = input()
#         k=my_string
#         # my_string1.upper()
#         # my_string=my_string1
#         rand1=random.randint(0,len(k))
#         for z in range(0,rand1):
#             rand=random.choice(k)
#             res=""
#
#             for j in range (0,len(k)):
#                 if rand==k[j]:
#                  res=k[:j]+rand+k[j:]
#                  k=res
#
#         l=[my_string,res]
#         l.sort()
#         ans=l[0]
#         ans=ans.upper()
#         print(f"Case #{i+1}: {ans}")
#         l=[]