import functools
from collections import deque
import sys

input = sys.stdin.readline

ans = ""
while True:
    inp = input().split()
    if len(inp) > 1:
        if(inp[0] == '0' and inp[1] == '0'):
            break
        ans += str(int(inp[0]) + int(inp[1])) + "\n"

    else:
        break

print(ans)