# Time-Module

import time

#to find initial time
inital=time.time()

#while loop time

k=0
while(k<=10):
    print(k," ",end="")
    time.sleep(2)
    #time.sleep() will pause program as per user requirement here it is 2 sec
    k+=1

inital2=time.time()
print("Time taken by loop is ",time.time()-inital)

for j in range(0,11):
    print(j," ",end="")
    time.sleep(2)
print("Time taken by loop is ",time.time()-inital2)

# To Print Local time of System
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

#time.time() give you current time, time.localtime() conver that to local time of system
# & finally time.asctime() convert that to readable time


