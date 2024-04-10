import sys

D = True
S = int(sys.stdin.readline())
M = [[0 for _ in range(S)] for _ in range(S)]
# if D: print(M)
for y in range(S):
    L = list(map(int, sys.stdin.readline().split()))
    # if D: print(L)
    for x in range(S):
        # print("L", L[i])
        M[y][x] = L[x]


only1 =  0
only0 = 0

def splitcnter(M):
    global only1
    global only0

    cnt1 = 0
    cnt0 = 0
    full = pow(len(M),2)
    for y in range(len(M)):
        for x in range(len(M)):
            if M[y][x] == 1:
                cnt1 += 1
            if M[y][x] == 0:
                cnt0 += 1

    if full == cnt1:
        only1 += 1
        return
    if full == cnt0:
        only0 += 1
        return
    else:
        half = len(M) / 2
        if half < 1:
            return

        half = int(half)
        M1 = [[0 for _ in range(half)] for _ in range(half)]
        M2 = [[0 for _ in range(half)] for _ in range(half)]
        M3 = [[0 for _ in range(half)] for _ in range(half)]
        M4 = [[0 for _ in range(half)] for _ in range(half)]
        for y in range(0, half):
            for x in range(0, half):
                M1[y][x] = M[y][x]
        splitcnter(M1)
        for y in range(0, half):
            for x in range(half, half*2):
                M2[y][x-half] = M[y][x]
        splitcnter(M2)
        for y in range(half, half*2):
            for x in range(0, half):
                M3[y-half][x] = M[y][x]
        splitcnter(M3)
        for y in range(half, half*2):
            for x in range(half, half*2):
                M4[y-half][x-half] = M[y][x]
        splitcnter(M4)


splitcnter(M)

print(only0)
print(only1)
