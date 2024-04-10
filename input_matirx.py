import sys

input = sys.stdin.readline

n = int(input())
s_list = [list(map(int,input().split())) for _ in range(n)]

print(s_list)