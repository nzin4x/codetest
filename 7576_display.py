import sys
import copy

X, Y = map(int, sys.stdin.readline().split())
Q = list(list(map(int, sys.stdin.readline().split())) for _ in range(Y))

lastwelldonecnt = 0
days = 0
notpossible = False


def expandtomato(Q):
    global lastwelldonecnt, days, notpossible

    # current status
    needtry = False
    welldonecnt = 0
    for y in range(Y):
        for x in range(X):
            if Q[y][x] == 0:
                needtry = True
            if Q[y][x] == 1:
                welldonecnt += 1

    if (welldonecnt == lastwelldonecnt):
        # no more expand
        if needtry:
            notpossible = True
        return

    lastwelldonecnt = welldonecnt

    # print("days", days)
    # for y in range(Y):
    #     for x in range(X):
    #         print("%3d" % Q[y][x],end="")
    #     print("")

    days += 1

    # expand
    Q2 = copy.deepcopy(Q)
    if needtry:
        for y in range(Y):
            for x in range(X):
                if Q[y][x] == 1:
                    if x > 0 and Q[y][x - 1] == 0: Q2[y][x - 1] = 1 # left
                    if x < X - 1 and Q[y][x + 1] == 0: Q2[y][x + 1] = 1 #right
                    if y > 0 and Q[y - 1][x] == 0: Q2[y - 1][x] = 1 #up
                    if y < Y - 1 and Q[y + 1][x] == 0: Q2[y + 1][x] = 1 #down

    Q = Q2
    expandtomato(Q)


expandtomato(Q)
if notpossible:
    print(-1)
else:
    print(days - 1)

