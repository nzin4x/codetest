import sys
from collections import deque

C = int(input())
S = [0 for _ in range(C + 1)]
M = [0 for _ in range(C + 1)]
for i in range(1, C + 1):
    S[i] = int(sys.stdin.readline())

# print(S)
if C == 1:
    print(S[1])
    exit(0)

M[0] = 0
M[1] = S[1] + S[0]
M[2] = max(S[1] + S[2], S[2])  # 한번에 2계단 오르는게 무조건 크겠지만 S[1] 이 음수일 수 있는 경우도 고려

for i in range(3, C + 1):
    # M[i] 가 가장 max 가 될 수 있는 것만 계속 저장해 가면서 다음을 찾는다.
    M[i] = S[i] + max(S[i - 1] + M[i - 3], M[i - 2]);
    # print(M)

print(M[-1])
