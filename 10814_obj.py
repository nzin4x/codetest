import sys

input = sys.stdin.readline
print = sys.stdout.write

qc = int(input())
ans = ""

list = []

for i in range(qc):
    list.append(input().split())

list = sorted(list, key=lambda x: int(x[0]))

for i in range(qc):
    ans += list[i][0] + " " + list[i][1] + "\n"


print(ans)
