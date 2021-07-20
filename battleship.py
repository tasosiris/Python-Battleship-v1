import math
import random
import sys


Player = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]


ComBot = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]

totalPlayer = 0

# Player_setting_first_ship-----------------------------------------------------------------------------------------------


while True:
    x1a, y1a = input(
        "Where do you want to place the front of your first ship: ").split()

    x1a = int(x1a)
    y1a = int(y1a)

    x1b, y1b = input(
        "Where do you want to place the back of your first ship(keep in mind that the first ship is 5 blocks long): ").split()

    x1b = int(x1b)
    y1b = int(y1b)

    x1 = abs(x1a - x1b)
    y1 = abs(y1a - y1b)

    distance1 = math.sqrt(x1**2 + y1**2)

    already = 0

    for i in range(x1+1):
        for j in range(y1+1):
            already = already + Player[i+x1a][j+y1a]

    if distance1 != 4:
        print("The blocks you chose are not 5 blocks apart! "
              "Try again!")

    elif already != 0:
        print("You have already placed another ship in these blocks"
              "Try again!")

    else:
        break

for i in range(x1+1):
    for j in range(y1+1):
        Player[i+x1a][j+y1a] = 1

print("The ship is placed")

print(distance1)
for line in Player:
    print(*line)

totalPlayer = totalPlayer + 5


# Player_setting_second_ship-----------------------------------------------------------------------------------------------


while True:
    x2a, y2a = input(
        "Where do you want to place the front of your second ship: ").split()

    x2a = int(x2a)
    y2a = int(y2a)

    x2b, y2b = input(
        "Where do you want to place the back of your second ship(keep in mind that the second ship is 3 blocks long): ").split()

    x2b = int(x2b)
    y2b = int(y2b)

    x2 = abs(x2a - x2b)
    y2 = abs(y2a - y2b)

    distance2 = math.sqrt(x2**2 + y2**2)

    already = 0

    for i in range(x2+1):
        for j in range(y2+1):
            already = already + Player[i+x2a][j+y2a]

    if distance2 != 2:
        print("The blocks you chose are not 3 blocks apart! "
              "Try again!")

    elif already != 0:
        print("You have already placed another ship in these blocks"
              "Try again!")

    else:
        break

for i in range(x2+1):
    for j in range(y2+1):
        Player[i+x2a][j+y2a] = 1

print("The ship is placed")

print(distance2)
for line in Player:
    print(*line)

totalPlayer = totalPlayer + 3


# Player_setting_third_ship-----------------------------------------------------------------------------------------------


while True:
    x3a, y3a = input(
        "Where do you want to place the front of your third ship: ").split()

    x3a = int(x3a)
    y3a = int(y3a)

    x3b, y3b = input(
        "Where do you want to place the back of your third ship(keep in mind that the third ship is 2 blocks long): ").split()

    x3b = int(x3b)
    y3b = int(y3b)

    x3 = abs(x3a - x3b)
    y3 = abs(y3a - y3b)

    distance3 = math.sqrt(x3**2 + y3**2)

    already = 0

    for i in range(x3+1):
        for j in range(y3+1):
            already = already + Player[i+x3a][j+y3a]

    if distance3 != 1:
        print("The blocks you chose are not 2 blocks apart! "
              "Try again!")

    elif already != 0:
        print("You have already placed another ship in these blocks"
              "Try again!")

    else:
        break

for i in range(x3+1):
    for j in range(y3+1):
        Player[i+x3a][j+y3a] = 1

print("The ship is placed")

print(distance3)
for line in Player:
    print(*line)

totalPlayer = totalPlayer + 2


# Player_setting_forth_ship-----------------------------------------------------------------------------------------------


while True:
    x4, y4 = input(
        "Where do you want to place your forth ship: ").split()

    x4 = int(x4)
    y4 = int(y4)

    if Player[x4][y4] == 1:
        print("You have already placed another ship in this block"
              "Try again!")

    else:
        break

Player[x4][y4] = 1

print("The ship is placed")

for line in Player:
    print(*line)

totalPlayer = totalPlayer + 1


# Player_setting_forth_ship-----------------------------------------------------------------------------------------------


while True:
    x5, y5 = input(
        "Where do you want to place your forth ship: ").split()

    x5 = int(x5)
    y5 = int(y5)

    if Player[x5][y5] == 1:
        print("You have already placed another ship in this block"
              "Try again!")

    else:
        break

Player[x5][y5] = 1

print("The ship is placed")

for line in Player:
    print(*line)

totalPlayer = totalPlayer + 1


# gameplay--------------------------------------------------------------------------------------------------------

# The_player_attaking---------------------------------------------------------------------------

totalComBot = 12

while totalComBot > 0 or totalPlayer > 0:

    x, y = input("Choose your target square: ").split()

    x = int(x)
    y = int(y)

    if int(ComBot[x][y]) == 1:
        print("You hit a ship!")
        ComBot[x][y] = 0
        totalComBot = totalComBot - 1
    else:
        print("You missed! Wait for your turn and try again!")

    print("The other player's board:")
    for line in ComBot:
        print(*line)

# The_bot_attaking---------------------------------------------------------------------------

    x = random.randint(0, 9)
    y = random.randint(0, 9)

    x = int(x)
    y = int(y)

    if int(Player[x][y]) == 1:
        print("A ship of yours just got hit!")
        Player[x][y] = 0
        totalPlayer = totalPlayer - 1
    else:
        print("The other player missed!!")

    print("Your board:")
    for line in Player:
        print(*line)

# results

if totalPlayer == 0:
    print("You lost!")
else:
    print("You won!")
