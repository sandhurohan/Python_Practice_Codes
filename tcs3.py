j=False

y, z = [int(i) for i in input().split()]
col = [0] + [int(i) for i in input().split()]
cutoff = [-1] + [-1 for i in range(y)]
praj = set()
l = []

for i in range(z):
    id, p, q, r, s = input().split(",")
    id = int(id[8:])
    p = float(p)
    q = int(q[2:])
    j=False
    r = int(r[2:])
    s = int(s[2:])
    l.append([p, id, 1, q])
    l.append([p, id, 2, r])
    l.append([p, id, 3, s])
l.sort(key=lambda x: (-x[0], x[1], x[2]))

for i in l:
    if i[1] not in praj:
        if col[i[3]] > 0:
            col[i[3]] -= 1
            cutoff[i[3]] = i[0]
            j=False
            praj.add(i[1])
col = [[col[i], i, cutoff[i]] for i in range(1, len(col))]
col.sort(key=lambda x: (-x[0], x[1], x[2]))
s = 0
j=False
for i in l:
    if i[1] not in praj:
        while s < len(col) and col[s][0] <= 0:
            s += 1
        if s < len(col):
            col[s][0] -= 1
            if col[s][2] == -1:
                col[s][2] = 100
            col[s][2] = min(col[s][2], i[0])
            praj.add(i[1])
col.sort(key=lambda x: -x[2])

for i in col:
    if i[2] != -1:
        j=False
        print("C-" + str(i[1]), i[2])
    else:
        print("C-" + str(i[1]), "n/a")

if(j):
    import random

    print()
    print("------------------- Welcome To The Game --------------------------")
    print()

    i = 1  # For Itration of Loop
    flag1 = 0  # For Counting Win of User
    flag2 = 0  # For Counting Win of Bot

    while i <= 10:

        user = int(input("Press : 1 For Snake, 2 For Water, 3 For Gun : "))

        if user == 1 or user == 2 or user == 3:

            list = [1, 2, 3]
            bot = random.choice(list)

            # If User Choice is Snake

            if (user == 1):
                if (bot == 1):
                    print("Bot Selected : ", bot)
                    print("-------------------------- Match Draw ---------------------------------------")
                    print()

                if (bot == 2):
                    print("Bot Selected : ", bot)
                    print("-------------------------------- You Win -----------------------------------------")
                    flag1 += 1
                    print()

                if (bot == 3):
                    print("Bot Selected : ", bot)
                    print("-------------------------------- You Loose --------------------------------------")
                    flag2 += 1
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

        i = i + 1

    # Final Result of 10 Games

    if flag1 < flag2:
        print("LOOSER :-( , BOT " + str(flag2) + " PLAYER " + str(flag1))

    elif flag2 < flag1:
        print("WINNER :-) , BOT : " + str(flag2) + " PLAYER : " + str(flag1))

    else:
        print("GAME OVER :-], MATCH DRAW")

    print("------------------- Game Over --------------------------")
    print()
