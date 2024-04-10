from collections import deque

n, m = map(int, input().split())
map_arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    map_arr[i] = list(map(int, input().split()))

visited = set()
ways = [(1, 0), (0, 1), (0, -1), (-1, 0)]

class Way:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def __hash__(self):
        return self.x * 100 + self.y

    def __eq__(self, another):
        return self.x * 100 + self.y == another.x * 100 + another.y

class PositionChecker:
    def __init__(self, limit_x, limit_y, map_arr):
        self.limit_x = limit_x
        self.limit_y = limit_y
        self.map_arr = map_arr

    def __str__(self):
        return f'{self.limit_x},{self.limit_y}'

    def isInMap(self, p: Position):
        if p.x >= 0 and p.x < self.limit_x and p.y >= 0 and p.y < self.limit_y:
            return True
        else:
            return False

    def isValidWay(self, p: Position):
        if self.map_arr[p.y][p.x] == 1:
            return True
        else:
            return False

    def valid(self, p: Position):
        return self.isInMap(p) and self.isValidWay(p)


ways = [Way(1, 0), Way(0, 1), Way(0, -1), Way(-1, 0)]

pc = PositionChecker(m, n, map_arr)

current_pos = Position(0, 0)
for y in range(pc.limit_y):
    for x in range(pc.limit_x):
        if map_arr[y][x] == 2:
            current_pos = Position(x, y)

# init
path_cnt = dict()
path_cnt[current_pos] = 0
visited.add(current_pos)
q = deque()
q.append(current_pos)


# bfs
while q:
    current_pos = q.popleft()

    # self check
    for move in ways:
        next_candidate = Position(current_pos.x + move.x, current_pos.y + move.y)
        if pc.isInMap(next_candidate) and next_candidate not in visited:
            if not pc.isValidWay(next_candidate):
                path_cnt[next_candidate] = 0
            else:
                prev_pos = current_pos

                visited.add(next_candidate)
                path_cnt[next_candidate] = path_cnt[prev_pos] + 1

                q.append(next_candidate)

            # print(f'{next_candidate} : {path_cnt[next_candidate]}')

# print(f'{path_cnt[Position(m - 1, n - 1)]}')
for y in range(pc.limit_y):
    for x in range(pc.limit_x):
        if path_cnt.get(Position(x,y)) != None and path_cnt.get(Position(x,y)) >= 0:
            print('%3d' % path_cnt.get(Position(x,y)), end=" ")
            # print('%d' % path_cnt.get(Position(x,y)), end=" ")
        else:
            if map_arr[y][x] == 0:
                print('%3d' % 0, end=" ")
                # print('%d' % 0, end=" ")
            else:
                print('%3d' % -1, end=" ")
                # print('%d' % -1, end=" ")

    print()