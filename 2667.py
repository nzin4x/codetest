import sys

C = int(input())
M = [[] for _ in range(C)]
for i in range(C):
   M[i] = list(map(int,list(input())))

V = [[0 for _ in range(C)] for _ in range(C)]
Move = [(-1, 0), (1,0), (0, -1), (0, 1)]


def findSiblings(x, y, _GrpNum):
    V[y][x] = 1

    for m in Move:
        nx, ny = x + m[0], y + m[1]
        if nx >=0 and ny >=0 and nx < C and ny < C and V[ny][nx] == 0 and M[ny][nx] == 1:
            global GrpTot
            GrpTot[_GrpNum-1] += 1

            # for _y in range(C):
            #     sys.stdout.write('\n')
            #     for _x in range(C):
            #         if V[_y][_x] == 1:
            #             sys.stdout.write(str(_GrpNum))
            #         else:
            #             sys.stdout.write('0')
            # sys.stdout.write('\n')


            findSiblings(nx, ny, _GrpNum)

GrpNum = 0
GrpTot = []
for y in range(C):
    for x in range(C):
        if V[y][x] == 0 and M[y][x] == 1:
            GrpNum += 1
            GrpTot.append(1)
            findSiblings(x, y, GrpNum)

            # for _y in range(C):
            #     sys.stdout.write('\n')
            #     for _x in range(C):
            #         if V[_y][_x] == 1:
            #             sys.stdout.write(str(GrpNum))
            #         else:
            #             sys.stdout.write('0')
            # sys.stdout.write('\n')

print(len(GrpTot))
GrpTot = sorted(GrpTot)
for v in GrpTot:
    print(v)


