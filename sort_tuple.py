import functools
from heapq import *

lst = [(3,2), (3,1)]

def compx(x, y):
    print("index 0 : ", x[0], y[0])
    print("index 1 : ", x[1], y[1])

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


lst.sort(key=functools.cmp_to_key(compx))

print(lst)