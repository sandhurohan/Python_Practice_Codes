n=int(input())
mn=int(input())
mx=int(input())

if mn==mx or mn>mx:
    print("Invalid Range")

else:
    for i in range(mn,mx+1):
        if n%i==0:
            print(f"{i} is divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")