import sys

N = int(sys.stdin.readline())
M = [[0 for _ in range(N)] for _ in range(N)]

for y in range(N):
    M[N - y - 1] = list(map(int, list(sys.stdin.readline().strip())))
    # print(M[y])

ans = ""
parts = [(-1, 0), (0, 0), (-1, -1), (0, -1)]


# 다 같은지 체크하고 안 같으면 그 부분만 나눈다.
def checkSame(sx, ex, sy, ey):
    # print(f'checksame {sx}, {ex}, {sy}, {ey}')
    global M
    base = M[sy][sx]

    for y in range(sy, ey):
        for x in range(sx, ex):
            if base != M[y][x]:
                return False

    # print('same!')
    return True


def dive(sx, ex, sy, ey):
    global M, parts, ans

    base = M[sy][sx]
    # 가장 작게 나뉘면, 그 숫자의 집합을 그대로 정답지에 추가한다.
    if sx + 1 == ex or checkSame(sx, ex, sy, ey):
        # print(f'base is {base}')
        ans += str(base)
        return

    # print(f'print not same area {sx},{ex},{sy},{ey}')

    # for y in range(sy, ey):
    #     for x in range(sx, ex):
    #         sys.stdout.write(str(M[y][x]) + " ")
    #     sys.stdout.write('\n')

    # devide and ask again
    sl = (ex - sx) // 2

    ans += "("
    for part in parts:
        # print(f'check part {part} for {sl} size')
        # print(f'devide and check part from ====> {sx + sl + part[0] * sl}, {sx + sl+ (part[0] + 1) * sl}, {sy + sl + part[1] * sl}, {sy + sl + (part[1] + 1) * sl}')

        dive(sx + sl + part[0] * sl, sx + sl + (part[0] + 1) * sl, sy + sl + part[1] * sl,
             sy + sl + (part[1] + 1) * sl)
    ans += ")"



dive(0, len(M), 0, len(M))
print(f'{ans}')
