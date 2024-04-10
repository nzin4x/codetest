d = False
# 1번과 연결되어 있는 컴퓨터를 찾기
# 1 : 총 컴퓨터 갯수
# 2 : 연결 정보 갯수
# else : 정보

# 정렬해서 연결 정보를 만들어간다.
import functools
import sys
from collections import deque

def mycmp(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        if x[1] > y[1]:
            return 1
        else:
            return 0

pools = set()

def solve(q):
    q.sort(key=functools.cmp_to_key(mycmp))
    if d: print("sorted", q)

    pool = set({1})
    pools = {}
    pools[1] = pool

    if d: print('pools', pools)

    for v in q:
        nothing = True

        # pool adder
        for p in pools:
            if d : print('a pool tester in', pools[p],'for',v[0], 'or', v[1])
            if v[0] in pools[p]:
                pools[p].add(v[1])
                nothing = False
            if v[1] in pools[p]:
                pools[p].add(v[0])
                nothing = False

        if d: print('pools ', pools)

        # add new pool
        if nothing:
            pool = set({v[0], v[1]})
            if d: print('new pool added', pool)
            pools[v[0]] = pool

        # merge
        base = None
        for p in pools:
            if v[0] in pools[p] and v[1] in pools[p]:
                if base == None:
                    base = pools[p]
                else:
                    # merge
                    if d: print('merge', base, 'and', pools[p])
                    base = base.union(pools[p])
                    if d: print('merged', base)
                    # pools[min(pools[p])] = None
                    pools[min(base)] = base

    return len(pools[1])


# live 처리기
pc = 10
qc = 4
q = '''
1 2
2 3
4 5
6 8
8 4
4 3
'''

# input 처리기
pc = int(input())
qc = int(input())
q = ""
for i in range(qc):
   q += sys.stdin.readline()

lst = q.strip().split('\n')
nset = set()

if d: print("lst : ", lst)
for v in lst:
    a, b = map(int, v.split())
    nset.add((a, b))
    # nset.add((b, a))

if d: print("nset : ", nset)
nlist = list(nset)

if d: print("nlist : ", nlist)

cnt = solve(nlist) - 1

print(cnt)