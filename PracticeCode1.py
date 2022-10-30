#--------------------------------- Practice Code 1 -------------------------------------------
print()
print("----------------------------------------- Problem 1 -----------------------------------")
print()
present=int(input("Please Enter Present Year : "))
year=int(input("Please Enter Your Birth Year : "))
age = int(input("Enter The Year To Calculate Age :"))

if year>=1900 and year<=9999 and present>=1900 and present<=9999 and age>=1900 and age<=9999:
    if present<year:
        print("You are not Born Yet!!")

    elif present-year>200:
        print("You Seems Oldest Person Alive")

    else:
        year100 = year + 100
        print(f"You Will Turn 100 Years Old in : {year100} ")
        ans = age - year
        print(f"Your Current Age is :{ans}")

else:
    print("Please Enter Valid Years !!")



