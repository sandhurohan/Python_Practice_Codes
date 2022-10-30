s1=set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)

s2=set()
s2.add(1)
s2.add(2)
s2.add(5)
s2.add(6)

print("The Values of Set Are : ",s1)
s1.remove(4)

print("The Updated Values of Set Are : ",s1)

print("The Minimum Values of Set Are : ",min(s1))

print("The Maximum Values of Set Are : ",max(s1))

print("The Intersection Values of Set Are : ",s2.intersection(s1))

print("The Union Values of Set Are : ",s2.union(s1))
