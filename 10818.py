import functools
from collections import deque
import sys

input = sys.stdin.readline

input() # drop question list
lst = list(map(int, input().split()))

print(str(min(lst)) + " " + str(max(lst)))