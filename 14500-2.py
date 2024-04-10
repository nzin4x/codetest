import sys
from pprint import pprint


tetros = [[[1,1,1,1]],
          [[1],
           [1],
           [1],
           [1]],
          [[1,1],
           [1,1]],
          [[1,0],
           [1,0],
           [1,1]],
          [[1,1],
           [1,0],
           [1,0]],
          [[0,1],
           [0,1],
           [1,1]],
          [[1,1],
           [0,1],
           [0,1]],
          [[1,1,1],
           [0,0,1]],
          [[1,1,1],
           [1,0,0]],
          [[0,0,1],
           [1,1,1]],
          [[1,0,0],
           [1,1,1]],
          [[1,0],
           [1,1],
           [0,1]],
          [[0,1],
           [1,1],
           [1,0]],
          [[1,1,0],
           [0,1,1]],
          [[0,1,1],
           [1,1,0]],
          [[1,1,1],
           [0,1,0]],
          [[0,1,0],
           [1,1,1]],
          [[1,0],
           [1,1],
           [1,0]],
          [[0,1],
           [1,1],
           [0,1]],
           ]


# print(M)

Y, X = map(int, sys.stdin.readline().strip().split())
M = Matrix = [[0 for _ in range(X)] for _ in range(Y)]
V = Visited = [[0 for _ in range(X)] for _ in range(Y)]
GV = GlobalVisited = set()

for y in range(Y):
    M[y] = list(map(int, sys.stdin.readline().strip().split()))

# print(M)

MAX = 0
for y in range(Y):
    for x in range(X): # for starting point
        for tetro in tetros: # with every tetros
            # bybpass overflow
            sum = 0
            tetroheight = len(tetro)
            tetrowidth = len(tetro[0])

            if x + tetrowidth - 1 >= X  or y + tetroheight - 1 >= Y :
                continue

            for ty in range(tetroheight): # if matches with 1
                for tx in range(tetrowidth):
                    if tetro[ty][tx] == 1:
                        # print('current M value of (',x+tx,',',y+ty,') is ',M[y+ty][x+tx], 'with current tetro width', tetrowidth, 'tetro height', tetroheight, 'starting position (',x,',',y,') and check position (',x+tx,',',y+ty,') and maxrix size (',X,',',Y,')')
                        sum += M[y+ty][x+tx]

            # print('and sum is ', sum)
            MAX = max(sum, MAX)

print(MAX)




