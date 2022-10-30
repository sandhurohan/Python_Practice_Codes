#Guess_Game

print("Guess The No. in 5 Attempts ")
guess=25
flag=1;
while(flag<=5):
    print("Guess The Number : ",end="")
    n=int(input())
    if n==guess:
        print("Congrats You Win The Game :)")
        break

    elif n<guess:
        print("TRY AGAIN","Entered No. is Less Than Required No. & Remaining Guess : ",5-flag)
        flag = flag + 1
        continue

    else:
        print("Entered No. is More Than Required No. & Remaining Guess : ",5-flag)
        flag = flag + 1
        continue
if flag>5:
    print("Game Over :(")