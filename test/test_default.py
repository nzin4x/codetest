import functools
from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write


def solve(lq=None, q=None, lt=None, t=None):

    lq = lq if lq != None else input().strip()
    q = q if q != None else input().strip()
    lt = lt if lt != None else input().strip()
    t = t if t != None else input().strip()

if __name__ == '__main__':
    ans = solve()
    print(str(ans))

def test_ex_1():
    assert solve(lq="10", q="6 3 2 10 10 10 -10 -10 7 3", lt="8", t="10 9 -5 2 3 4 5 -10") == "3 0 0 1 2 0 0 2"
