import heapq
import sys
from collections import deque

C = int(sys.stdin.readline().strip())
Q = []

for _ in range(C):

    N = int(sys.stdin.readline().strip())
    AN = abs(N)
    P = 0

    if N != 0:
        heapq.heappush(Q, (AN, N))
    elif N == 0:
        if Q:
            P = heapq.heappop(Q)
            print(P[1])
        else:
            print(0)




