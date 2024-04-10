import sys
from collections import deque

X, Y = map(int, sys.stdin.readline().split())
Q = list(list(map(int, sys.stdin.readline().split())) for _ in range(Y))
dq = deque([])

moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]

# setup
for y in range(Y):
    for x in range(X):
        if Q[y][x] == 1:
            dq.append((y, x))


def bfs():
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            nx = x + moveX[i]
            ny = y + moveY[i]

            if 0 <= nx < X and 0 <= ny < Y:
                if Q[ny][nx] == 0:
                    Q[ny][nx] = Q[y][x] + 1
                    dq.append((ny, nx))


bfs()
ans = 0
notDone = False

for y in range(Y):
    for x in range(X):
        if Q[y][x] == 0:
            notDone = True

        ans = max(ans, Q[y][x])

if notDone:
    print(-1)
else:
    print(ans-1)
