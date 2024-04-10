import functools
from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write
qc = int(input())
ans = ""
lst = []

for i in range(qc):
    lst.append(list(map(int, input().split())))

def fn_xsort(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            # not given case.
            return 0

lst = sorted(lst, key=functools.cmp_to_key(fn_xsort))

for i in range(qc):
    ans += str(lst[i][0]) + " " + str(lst[i][1]) + "\n"

print(ans)

