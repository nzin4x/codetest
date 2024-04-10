from collections import deque

n, j = map(int, input().split())
# print(n)
# print(list(range(0,n)))

ans = "<"
dq = deque(list(range(1,n + 1)))

# print(len(dq))
pnt = 0
while len(dq) > 0:
    pnt += j - 1
    pnt = pnt % len(dq)
    # print(dq[pnt])
    ans += str(dq[pnt]) + ", "
    dq.remove(dq[pnt])


print(ans[:-2] + ">")




