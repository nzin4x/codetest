from collections import deque

dmax = 0

def solve(n, k) -> int:
    if n == k:
        return 0

    q = deque([])
    visited = [False] * dmax

    # init
    q.append(n)
    visited[n] = True
    depth = 0

    while q:
        crnt = q.popleft()

        # next candidate
        nxt = crnt - 1
        if nxt >= 0 and visited[nxt] == False:
            q.append(nxt)
            visited[nxt] = True

        nxt = crnt + 1
        if nxt < len(visited) and visited[nxt] == False:
            q.append(nxt)
            visited[nxt] = True

        nxt = crnt * 2
        if nxt < len(visited) and visited[nxt] == False:
            q.append(nxt)
            visited[nxt] = True

        depth += 1

        if k in q:
            return depth


# 5 17 -> 4
# n, k = map(int, input().split())
# n, k = 100000, 100000
# n, k = 1,0
n, k = 5, 17

imax = 100_100
dmax = min(max(n, k) * 2 + 1, imax)

# for i in range(0, 10000):
#     for j in range(i, 10000):
#         #print(i, j, solve(i,j))
#         pass

print(solve(n,k))