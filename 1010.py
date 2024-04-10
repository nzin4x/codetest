# x 개 중에 y 개를 선택할 확률, 단 역상 선택 불가하므로 2로 나눈다.
import math


def choosecnt(x, y):
    return math.factorial(x) // (math.factorial(y) * math.factorial(x-y))

qc = int(input())
ans = ""
for i in range(qc):
    n, m = map(int, input().split())
    ans += str(choosecnt(m,n)) + "\n"

print(ans)

# 검산
# for j in range(1, 30 + 1):
#     for i in range(1, 30 + 1):
#         if (i > j):
#             continue
#         else:
#             print('n ', i, 'm ', j, ' ', choosecnt(j, i))
#



