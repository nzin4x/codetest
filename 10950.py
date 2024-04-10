import functools
from collections import deque
import sys

input = sys.stdin.readline

qc = int(input())
ans = ""

for i in range(qc):
    a, b = map(int, input().split())
    ans += str(a + b) + "\n"

print(ans)

