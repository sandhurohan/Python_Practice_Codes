list1=["Harry","Larry","Marry"]
list2=[["Harry","1"],["Larry","2"],["Marry","3"]]

for item in list1:
    print(item)

for item1,item2 in list2:
    print(item1," has ",item2," Cars")

dict1=dict(list2)
for item1,item2 in dict1.items():
    print(item1,"has",item2,"guns")