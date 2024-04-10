M=int(input())
N=int(input())
H = []
Q = [[] for _ in range(M + 1)]


def dfs(n):
    H.append(n)
    for q in Q[n]:
        if q not in H:
            dfs(q)

for i in range(N):
    A, B = map(int, input().split())
    Q[A].append(B)
    Q[B].append(A)


dfs(1)
print(Q)
print(H)
print(len(H) - 1)