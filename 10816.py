import functools
from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

qc = (input()) # passs first line
ans = ""
hc = {}

qs = list(map(int, input().split()))
for v in qs:
    if v in hc:
        hc[v] += 1
    else:
        hc[v] = 1

# match count
mc = (input()) # pass
ms = list(map(int, input().split()))

for v in ms:
    if v in hc:
        ans += str(hc[v]) + " "
    else:
        ans += "0" + " "

print(ans)



