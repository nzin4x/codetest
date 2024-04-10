# 최대힙

import heapq
import sys

heap = []

qcnt = int(sys.stdin.readline())
ans = ""
for _ in range(qcnt):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(heap) == 0:
            ans += "0\n"
        else:
            p = heapq.heappop(heap)
            ans += str(-p) + "\n"
    else:
        heapq.heappush(heap, -n)
print(ans)
