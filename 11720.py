import functools
from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write
qc = input().strip()
qs = input().strip()

ans = 0
cnt = 0
for q in list(qs):
    ans = int(q) + ans
    cnt = cnt + 1

print(str(ans))
# print(f'caled in {cnt} counter')




