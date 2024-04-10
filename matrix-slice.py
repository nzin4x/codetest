# 코테에서는 numpy 를 제하지 않는다.
from numpy import array


M = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

M0 = array(M)
M1 = M0[0:2,0:2].copy()

print(M1)
