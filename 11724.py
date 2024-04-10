import sys
sys.setrecursionlimit(5000)


M, N = map(int, input().split())
edges = [[] for _ in range(M + 1)]
answers = []
passed = [0 for _ in range(M + 1)]

for _ in range(N):
    _from, _to = map(int, sys.stdin.readline().strip().split())
    # edges[_from].append(_to)
    edges[_from].append(_to)
    edges[_to].append(_from)


def dfs(n):
    passed[n] = 1

    for e in edges[n]:
        if not passed[e]:
            dfs(e)

ansgrp = 0

# print(edges)
for i in range(1, len(edges)):
    _e = edges[i]
    if not passed[i]:
        # print('dfs!', i)
        dfs(i)
        ansgrp += 1

# print(edges)
print (ansgrp)

