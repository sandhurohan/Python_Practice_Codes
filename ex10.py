#Harry Way
import requests
import pickle

data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
l1=data.split("\n")
l2=[]
for i in range(0,len(l1)):
    x=l1[i].split(",")
    l2.append(x)

# picklimg & Unpickling
f1=open("f1.pkl","wb")
pickle.dump(l2,f1)
f1.close()

f1=open("f1.pkl","rb")
print(pickle.load(f1))
f1.close()

# Ordinary Way

# import requests
#
# # print(r)
#
# #For Writing
#
# ex10=open("ex10.txt","w")
# r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# ex10.write(r)
# ex10.close()
#
# # For Reading
# ex10=open("ex10.txt","r")
# content=ex10.readlines()
# length=len(content)
# l1=[]
# for i in range(0,length):
#         x=content[i].split(",")
#         l1.append(x)
# print(l1)
# print(length)
# ex10.close()
#
