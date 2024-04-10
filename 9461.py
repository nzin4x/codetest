QC = int(input())

M=[1 for _ in range(101)]

M[1] = 1
M[2] = 1
M[3] = 1
M[4] = 2
M[5] = 2

def solve(N : int):
    if N <= 5:
        return M[N]
    else:
        for i in range(6, N + 1):
            M[i] = M[i - 1] + M[i - 5]

    return M[N]


for _ in range(QC):
    S = solve(int(input()))
    print(S)