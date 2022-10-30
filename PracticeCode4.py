#--------------------------------------- NEXT PALINDROME FUNCTION --------------------------------
print()
print("-------------------------- NEXT PALINDROME -------------------------------------")
print()
T=int(input("Enter No. Of test Cases : "))

# For Taking Input for Multiple Test Cases
for i in range(0,T):

    # Input of test case
    n = int(input())
    m=n

    # Actual Logic
    while True:
        n=int(n)+1
        n=str(n)
        if n==n[::-1]:
            print(f"Next Palindrome of {m} is : {n}")
            break
