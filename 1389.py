# 최단거리 알고리즘 에서 가중치가 0이나 1인 경우 bfs 로 풀 수 있다. dfs 는 안된다.
from collections import deque
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

shortest = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
kebin = [0 for _ in range(N + 1)]

def bfs_drive(_from, _to):
    dq = deque([])
    visited = [False for _ in range(N + 1)]

    dq.append((_from, 0))
    visited[_from] = True

    while dq:
        current_edge = dq.popleft()
        shortest[_from][current_edge[0]] = current_edge[1]

        for neighbor in graph[current_edge[0]]:
            if not visited[neighbor]:
                dq.append((neighbor, current_edge[1] + 1))
                visited[neighbor] = True


for _from in range(1, N+1):
    for _to in range(1, N+1):
        if _from != _to:
            if _from < _to:
                bfs_drive(_from, _to)
            elif _from > _to:
                shortest[_from][_to] = shortest[_to][_from]

# print(shortest)

minpath = 99999
hq = []

for _from in range(1, N+1):
    for _to in range(1, N+1):
        if shortest[_from][_to] > 0:
            kebin[_from] += shortest[_from][_to]
    minpath = min(minpath, kebin[_from])
    heapq.heappush(hq,(minpath,_from))

(m, p) = heapq.heappop(hq)
print(p)





