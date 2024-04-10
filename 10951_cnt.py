import functools
from collections import deque
import sys

input = sys.stdin.readline

ans = ""
while True:
    inp = input().split()
    if len(inp) > 1:
        ans += str(int(inp[0]) + int(inp[1])) + "\n"
    else:
        break

print(ans)