import copy
import itertools
import sys
from collections import deque


done = 0
def dfs(x, dq):
    global done
    n = dq.popleft()

    if (x - n >= 0):
        x -= n
        if (x == 0):
            done += 1
            return


        for v in numx:
            if (x - v >= 0):
                dq.append(v)
                dfs(x, dq)


numx = [1,2,3]
def solve(x):
   dq = deque([])

   for v in numx:
       if (x - v >= 0):
           dq.append(v)
           dfs(x, dq)


# solve(10)
# print(done)

qcnt = int(sys.stdin.readline())
for _ in range(qcnt):
    done = 0
    solve(int(sys.stdin.readline()))
    print(done)
