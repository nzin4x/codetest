from collections import deque
import sys

input = sys.stdin.readline

qc = int(input())
hc = [0,0]
def fibo(n):
    if n == 0:
        if 0 in hc:
            hc[0] += 1
        else:
            hc[0] = 1
        return 0
    elif n == 1:
        if 1 in hc:
            hc[1] += 1
        else:
            hc[1] = 1
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)


ans = ""
for i in range(qc):
    n = int(input())
    hc = [0,0]
    fibo(n)
    ans += (str(hc[0]) + " " + str(hc[1])) + "\n"

print(ans)
