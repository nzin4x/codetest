# bfs breadth 너비 우선 탐색, queue가 다 달때까지, loop, stack
# dfs 깊이 우선 탐색, 재귀 (끝까지 들어가본다.)

# setup
from collections import deque

vertaxs, edges, top = map(int, input().split())
graph = [[] for _ in range(vertaxs + 1)]
for _ in range(edges): # 갈 수 있는 곳에 대한 마킹
    _from, _to = map(int, input().split())
    graph[_from].append(_to)
    graph[_to].append(_from)


def bfs(graph, visited, edge) -> str:
    dq = deque([])

    # init
    dq.append(edge)
    visited.add(edge)

    ans = ""

    while dq:
        current_edge = dq.popleft()
        ans += str(current_edge) + " "
        for neighbor in sorted(graph[current_edge]):
            if neighbor not in visited:
                dq.append(neighbor)
                visited.add(neighbor)

    return ans


def bfs_driver(graph, top) -> str:
    visited = set()
    ans = bfs(graph, visited, top)

    print(visited)
    return  ans


def dfs(graph, dq, visited, current_edge):
    visited.add((current_edge))
    visited_seq.append((current_edge))

    for neighbor in sorted(graph[current_edge]): # graph 만들 때 추가된 선로를 순서대로 방문 DFS, 먼저 깊게 들어간다. sorted 를 매번 하는 것은 안 좋을 듯
        if neighbor not in visited:
            dfs(graph, dq, visited, neighbor)


visited_seq = []

def dfs_driver(graph, top):
    visited = set()

    # init
    dq = deque([])
    dq.append(top)
    visited.add(top)
    visited_seq.append(top)

    dfs(graph, dq, visited, top)

    return " ".join(map(str, visited_seq))

ans_dfs = ""
def solve(graph, top):
    dfs_driver(graph, top)
    print(ans_dfs)
    ans = bfs_driver(graph, top)
    print(ans)



solve(graph, top)
