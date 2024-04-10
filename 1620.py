# dynamic programming bottom up
import sys

D = {}
DR = {}
PC, QC = map(int, input().split())

# setup
for i in range(1, PC + 1):
    aPoke = sys.stdin.readline().strip()
    D[i] = aPoke
    DR[aPoke] = i

for i in range(QC):
    q = sys.stdin.readline().strip()
    if q.isnumeric():
        print(D[int(q)])
    else:
        print(DR[q])
