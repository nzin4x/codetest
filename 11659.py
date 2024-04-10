import itertools
import sys

_, C=map(int, input().split())
N = list(map(int, sys.stdin.readline().strip().split()))
Sum = [0 for _ in range(len(N) + 1)]

Sum[0] = 0
for i in range(1, len(N) + 1):
    Sum[i] += N[i-1] + Sum[i-1]

# print(Sum)

for _ in range(C):
    S, E = map(int, sys.stdin.readline().strip().split())
    print(Sum[E] - Sum[S - 1])
