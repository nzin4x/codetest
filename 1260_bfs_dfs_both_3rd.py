import sys
from collections import deque

edge_cnt, vertex_cnt, initial_position = map(int, input().split())
connection = [[] for _ in range(edge_cnt + 1)]
q = deque()
visited = set()
visited_seq = list()

for i in range(vertex_cnt):
    _from, _to = map(int, input().split())
    connection[_from].append(_to)
    connection[_to].append(_from)

# print(connection)

# dfs

def dfs_visit(current_pos):
    visited.add(current_pos)
    visited_seq.append(current_pos)

    for next_candidate in sorted(connection[current_pos]):
        if next_candidate not in visited:
            dfs_visit(next_candidate)

dfs_visit(initial_position)

print(' '.join(map(str, visited_seq)))


# bfs
q = deque()
visited = set()
visited_seq = list()

q.append(initial_position)
visited.add(initial_position)
visited_seq.append(initial_position)

while q:
    current_position = q.popleft()
    for next_candidate in sorted(connection[current_position]):
        if next_candidate not in visited:
            q.append(next_candidate)
            visited.add(next_candidate)
            visited_seq.append((next_candidate))

print(' '.join(map(str, visited_seq)))

