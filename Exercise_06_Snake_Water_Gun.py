# Snake Water Gun
# 1. Snake Drink Water -- Snake Wins -- , 2. Gun Sink in Water -- Water Wins -- & Gun Shots Snake -- Gun Win --

import random
print()
print("------------------- Welcome To The Game --------------------------")
print()

i=1         # For Itration of Loop
flag1=0     # For Counting Win of User
flag2=0     # For Counting Win of Bot

while i<=10:

    user=int(input("Press : 1 For Snake, 2 For Water, 3 For Gun : "))

    if user==1 or user==2 or user==3:

        list=[1,2,3]
        bot=random.choice(list)

        #If User Choice is Snake

        if(user==1):
            if(bot==1):
                print("Bot Selected : ",bot)
                print("-------------------------- Match Draw ---------------------------------------")
                print()

            if (bot == 2):
                print("Bot Selected : ", bot)
                print("-------------------------------- You Win -----------------------------------------")
                flag1+=1
                print()

            if (bot == 3):
                print("Bot Selected : ", bot)
                print("-------------------------------- You Loose --------------------------------------")
                flag2+=1
                print()

        # If User Choice is Water

        if (user == 2):
            if (bot == 1):
                print("Bot Selected : ", bot)
                print("-------------------------------- You Loose ---------------------------------------")
                flag2 += 1
                print()

            if (bot == 2):
                print("Bot Selected : ", bot)
                print("-------------------------------- Match Draw --------------------------------------")
                print()

            if (bot == 3):
                print("Bot Selected : ", bot)
                print("--------------------------------- You Win ----------------------------------------")
                flag1 += 1
                print()

        # If User Choice is Gun

        if (user == 3):
            if (bot == 1):
                print("Bot Selected : ", bot)
                print("----------------------------------- You Win -----------------------------------------")
                flag1 += 1
                print()

            if (bot == 2):
                print("Bot Selected : ", bot)
                print("---------------------------------- You Loose ------------------------------------------")
                flag2 += 1
                print()

            if (bot == 3):
                print("Bot Selected : ", bot)
                print("--------------------------------- Match Draw ----------------------------------------")
                print()
    else:
        print("Invalid Option")

    i=i+1

# Final Result of 10 Games

if flag1<flag2:
    print("LOOSER :-( , BOT "+str(flag2) +" PLAYER "+str(flag1))

elif flag2<flag1:
    print("WINNER :-) , BOT : "+str(flag2) +" PLAYER : "+str(flag1))

else:
    print("GAME OVER :-], MATCH DRAW")

print("------------------- Game Over --------------------------")
print()

# All Rights Reserved @white_devil_61