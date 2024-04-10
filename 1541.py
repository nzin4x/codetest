# 괄호 필요 없는 듯. 그냥 첫번째 - 이후것은 모두 빼라.
import re

q = input()

minstart = -1
try :
    minstart = q.index('-')
except:
    pass


if (minstart >0):

    qs = list(map(int, re.split("[+]", string=q[0:minstart])))
    sum = 0
    for v in qs:
        sum += v

    qs = list(map(int, re.split("[+-]", string=q[minstart+1:])))
    for v in qs:
        sum -= v

    print(sum)

else:
    # 모두 더한다.
    qs = list(map(int, re.split("[+]", string=q)))

    sum = 0
    for v in qs:
        sum += v

    print(sum)