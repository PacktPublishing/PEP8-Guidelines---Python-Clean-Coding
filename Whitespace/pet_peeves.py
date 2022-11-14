players = [23, 54, 78, 19, 8]

food = {"bread": 5, "meat": 2, "orange": 6}

me = food["meat"]

a = players[1:3]
b = players[1:5:2]
c = players[:2:4]
d = players[1::3]
e = players[1:9:]


def pr(t):
    print(t)


pr(e)

player1 = players[1]
food["bread"] = 7
print(food["bread"])

x = 10
y = 11

if x == 4: print(x, y); x, y = y, x

x = 1
y = 2
long_variable = 3
