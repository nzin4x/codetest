from collections import deque

Y, X = map(int, input().split())
M = [[0 for _ in range(X)] for _ in range(Y)]
for i in range(Y):
    M[i] = list(map(int,list(input())))
    # print(M[i])



V = set()
V.add((0,0))
Q = deque([])
Q.append((0,0,1))
W = [(-1,0), (1,0), (0,1), (0,-1)]

while Q:
    C = Q.popleft()
    # print(f'current : {C}')
    x, y = C[0], C[1]
    # 사방으로
    for w in W:
        nx, ny = x + w[0], y + w[1]
        # 새로운 1이면 후보에 추가한다.
        if nx < X and ny < Y  and nx >=0 and ny >= 0 and (nx, ny) not in V and M[ny][nx] == 1:
            Q.append((nx, ny, C[2] + 1))
            V.add((nx, ny))
            # print(f'new way : {nx, ny} with depth {C[2] + 1}')

            if nx == X - 1 and ny == Y - 1:
                print(C[2] + 1)
