import sys
from collections import deque

edge_count, line_count, starting_point = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(edge_count + 1)]
q = deque([])
visited = list()

for _ in range(line_count):
    edge_start, edge_end = map(int, sys.stdin.readline().strip().split())
    graph[edge_start].append(edge_end)
    graph[edge_end].append(edge_start)

def dfs(current_edge):
    global visited
    visited.append(current_edge)

    candidates = graph[current_edge]
    candidates = sorted(candidates)

    for neighbor in candidates:
        if neighbor not in visited:
            dfs(neighbor)

def driver_dfs(graph, starting_point):
    global visited
    visited = list()

    dfs(starting_point)

    print(' '.join(map(str,visited)))


def bfs(q):
    while q:
        current_edge = q.popleft()
        visited.append(current_edge)

        candidates = graph[current_edge]
        candidates = sorted(candidates)

        for neighbor in candidates:
            if neighbor not in visited and neighbor not in q:
                q.append(neighbor)

def driver_bfs(graph, starting_point):
    global visited
    visited = list()

    q = deque([])
    q.append(starting_point)

    bfs(q)
    print(' '.join(map(str,visited)))

driver_dfs(graph, starting_point)
driver_bfs(graph, starting_point)





