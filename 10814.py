import functools
from collections import deque
import sys
from dataclasses import dataclass

input = sys.stdin.readline
print = sys.stdout.write

@dataclass
class AgeName:
    age: int = None
    name: str = None

qc = int(input())
q = deque([])
ans = ""

def fn_compare(x, y):
    return int(x.age) < int(y.age)

for i in range(qc):
    line = input().split()
    man = AgeName()
    man.age = line[0]
    man.name = line[1]

    q.append(man)


q = sorted(q, key=functools.cmp_to_key(fn_compare))
# sorted(q, key=cmp_to_key(fn_compare))

for i in range(qc):
    ans += q[i].age + " " + q[i].name + "\n"

print(ans)
