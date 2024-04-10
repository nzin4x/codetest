import functools
from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve(qc=None, qs=None):

    qc = qc if qc != None else input().strip()
    qs = qs if qs != None else input().strip()

    ans = 0
    cnt = 0
    qu = []
    for q in qs.split(' '):
        qu.append(int(q))

    max_point = max(qu)

    tot = 0
    for q in qs.split(' '):
        new_pnt = int(q) / max_point * 100
        tot = tot + new_pnt

    return tot / len(qs.split(' '))


if __name__ == '__main__':
    avg = solve()
    print(str(avg))

def test_ex_1():
    assert solve(qc="3", qs="40 80 60") == 75.0
    assert round(solve(qc="3", qs="10 20 30"), 2) == round(66.666667, 2)
