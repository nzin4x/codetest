# 최단거리 알고리즘

from collections import deque

MAX = 1000000
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
shortest = [[-1 for _ in range(N+ 1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # two-way graph
    graph[a].append(b) # 여기에 length 까지 결합하면 다익스트라
    graph[b].append(a)

# from 1 to 5
def dfs(_from, _to, dq, visited, depth):
    _current = dq.popleft()
    visited[_current] = True

    if _current == _to:
        if shortest[_from][_to] == -1:
            shortest[_from][_to] = MAX
        shortest[_from][_to] = min(shortest[_from][_to], depth)
        return
    else:
        depth += 1

    for v in graph[_current]:
        if not visited[v]:
            dq.append(v)
            dfs(_from,_to,dq, visited, depth)


def dfs_driver(_from, _to):
    dq = deque([])
    dq.append(_from)
    visited = [False for _ in range(N + 1)]

    dfs(_from, _to, dq, visited, 0)

shortcut = [0 for _ in range(N+1)]
minvals = MAX
for _from in range(1,N+1):
    for _to in range(1, N+1):
        if _from < _to:
            dfs_driver(_from, _to)
        elif _from > _to:
            shortest[_from][_to] = shortest[_to][_from]

        shortcut[_from] += shortest[_from][_to]
    minvals = min(minvals, shortcut[_from])

print(shortest)
print(shortcut)

for _from in range(1,N+1):
    if shortcut[_from] == minvals:
        print(_from)
        break






