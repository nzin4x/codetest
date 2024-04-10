import functools
import sys
from collections import deque

# 정을 1이 작은것와 2가 작은 것 순으로 한다.
def compx(x, y):

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
            return 0

def solve(str) -> list:
    lst = str.split('\n')

    hlst = []
    for v in lst:
        hlst.append(tuple(map(int, v.split())))

    hlst.sort(key=functools.cmp_to_key(compx))

    # [(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]
    print (hlst)

    rst = []
    for i in range(len(hlst)):
        current = hlst[i]
        if i < len(hlst) - 1 and hlst[i+1][0] < hlst[i][1] and hlst[i+1][1] <= hlst[i][1]:
            # 뒤의 것이 낫다. i 는 버려야 한다.
            pass
        elif i >= 1 and len(rst) > 0 and hlst[i][0] < rst[-1][1] and rst[-1][0] < rst[-1][1]:
            # 이전것 보다 일러서 이것은 추가 할 수 없다.
            pass
        else:
            # 이것이 낫다. 이것은 추가되어야 한다.
            rst.append(hlst[i])

    return rst



q = '''1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14 '''

# 반례
q = '''
1 5
1 7
2 3
3 4

'''

# qc = int(input())
# q = ""
# for i in range(qc):
#     q += sys.stdin.readline()

rst = solve(q.strip())
print(len(rst))