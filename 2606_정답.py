import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

V = [[] for _ in range(N + 1)]
Heap = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    V[a].append(b)
    V[b].append(a)

def dfs(n):
    Heap.append(n)
    for v in V[n]:
        if v not in Heap:
            dfs(v)

dfs(1)

print(len(Heap) - 1)



