# 이코드는 5번째 케이스를 하지 못한다.
import sys

Y, X = map(int, sys.stdin.readline().strip().split())
M = Matrix = [[0 for _ in range(X)] for _ in range(Y)]
V = Visited = [[0 for _ in range(X)] for _ in range(Y)]
GV = GlobalVisited = set()

W = Ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX = 0

for y in range(Y):
    M[y] = list(map(int, sys.stdin.readline().strip().split()))

print(M)

def dfs(visited, current_edge, sum, depth):
    depth += 1
    visited.append(current_edge)
    y, x = current_edge[1], current_edge[0]
    val = M[y][x]
    sum += val
    global MAX

    # print('current path ', visited, 'and depth ', depth)

    if len(visited) == 4:
        # completed mark sum and total visited as sorted

        visitcache = sorted(visited)

        if str(visitcache) in GV:
            # just next
            visited.pop()
            return

        if True:
            GV.add(str(visitcache))
            print(len(GV), visitcache, sum)
            if sum > MAX:
                MAX = sum

            # print("four reached with ", visited, sum)
            visited.pop()
            return

    # possible ways
    for w in W:
        # not overflow && not visited
        next_edge = (current_edge[0] + w[0], current_edge[1] + w[1])
        if next_edge[0] >= 0 and next_edge[1] >= 0 and next_edge[0] < X and next_edge[1] < Y and next_edge not in visited:
            # print("try next possibilities with next_edge",next_edge, " : ", visited, 'of current depth', depth)
            dfs(visited, next_edge, sum, depth)

    # print("end of possible ways : go previous and current sum ", sum, 'current depth', depth)
    visited.pop()


def drive_dfs(starting_point):
    visited = []
    dfs(visited, starting_point, 0, 0)
    # print(visited)


def maxSumIn4blocks(M):
    # for y in range(Y):
    #     for x in range(X):
    #         starting_point = (x, y)
    #         drive_dfs(starting_point)

    starting_point = (0,0)
    drive_dfs(starting_point)


maxSumIn4blocks(M)

print(MAX)
