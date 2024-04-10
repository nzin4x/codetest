import math

QC = int(input())


def solve():
    N, M, x, y = map(int, input().split())
    lcm = math.lcm(N, M)
    divcnt = 0
    x1, y1 = x, y

    # print (f'lcm {lcm}')
    while not (x1 == y1 or lcm == 0):
        divcnt += 1
        lcm -= N
        y1 += (M - N)
        y1 %= M
        # print (lcm, x1, y1)

    if x1 == y1:
        print(N * divcnt + x1)
        return

    divcnt = 0
    x2, y2 = x, y
    lcm = math.lcm(N, M)
    while not (x2 == y2 or lcm == 0):
        divcnt += 1
        lcm -= M
        x2 += (N - M)
        x2 %= M
        print (lcm, x2, y2)

    if x2 == y2:
        print(M * divcnt + y2)
        return
    else:
        print(-1)

for _ in range(QC):
    solve()