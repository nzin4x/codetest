import functools
from collections import deque
import sys
from dataclasses import dataclass

q = deque({})
q.append(2)
q.append(1)

q = sorted(q)

for i in q:
    print(i)