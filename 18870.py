import sys

Q = int(input())
M = list(map(int, sys.stdin.readline().split()))

N = sorted(M)
dm = {}
order = 0

# set map
for i in range(len(N)):
    if N[i] not in dm:
        dm[N[i]] = str(order)
        order += 1

for i in range(len(M)):
    M[i] = dm[M[i]]

print(" ".join(M))


