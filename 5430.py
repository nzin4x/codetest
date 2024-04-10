import sys
from collections import deque

QC = int(input())


def solve():
    D = True # True origin way, False reverse way
    CMD= list(sys.stdin.readline().strip())
    L = int(sys.stdin.readline())
    Q = sys.stdin.readline().strip()
    Q = Q.replace('[', '').replace(']','').strip()
    if L ==0:
        Q =  deque([])
    else:
        Q = deque(list(map(int,Q.split(','))))
    # print('Q')
    # print(Q)

    for c in CMD:
        if c == 'R':
            D = not D
            # print('do reverse')
            # print(D)
        elif c == 'D' and D and len(Q):
            Q.popleft()
            # print('pop left after ')
            # print(Q)
        elif c == 'D' and not D and len(Q):
            Q.pop()
            # print('pop right after ')
            # print(Q)
        else:
            # print('last cmd' + c)
            return 0, False

    Q = list(Q)
    if not D:
        Q.reverse()
        # print('reverse needed / after reverse')
        # print (Q)

    # print ('current Q before return ')
    # print (Q)

    return '[' + ','.join(map(str,list(Q))) + ']', True







for i in range(QC):
    val, ok = solve()
    if ok:
        print(val)
    else:
        print('error')