from collections import deque
import sys

input = sys.stdin.readline

def visitcounter(nn, r, c):
    cnt = 0
    for n in range(nn, 0, -1):
        if n == 1:
            if r == 0 and c == 0:
                pass
            elif r == 0 and c == 1:
                cnt += 1
            elif r == 1 and c == 0:
                cnt += 2
            elif r == 1 and c == 1:
                cnt += 3
        elif n > 1:
            half = pow(2,n)/2
            box = pow(2, n - 1) * pow(2, n - 1)
            # 2사분면
            if (r < half and c < half):
                continue
            # 1사분면
            elif (r < half and c >= half):
                cnt += box
                c -= pow(2, n-1)
                continue
            # 3사분면
            elif (r >= half and c < half):
                cnt += box * 2
                r -= pow(2, n-1)
                continue
            # 4사분면
            elif (r >= half and c >= half):
                cnt += box * 3
                r -= pow(2, n-1)
                c -= pow(2, n-1)
                continue

    return cnt

# print(visitcounter(2, 3, 1))
n, r, c = map(int, input().split())
print(visitcounter(n, r, c))



