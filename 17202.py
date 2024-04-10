# DP top down
from collections import deque

a = input()
b = input()

dq = deque([])
for i in range(0,8):
    dq.append(int(a[i]))
    dq.append(int(b[i]))

while True:
    ndq = deque([])

    for i in range(len(dq) - 1):
        n = (dq[i] + dq[i + 1]) % 10
        # print('new n : ', n)
        ndq.append(n)

    dq = ndq
    if 2 == len(ndq):
        break

print(''.join(map(str,ndq)))

