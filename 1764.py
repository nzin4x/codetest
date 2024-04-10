import sys

snh = set()
sns = set()

input = sys.stdin.readline

n, m = map(int, input().split())
for i in range(n):
    snh.add(input())
for i in range(m):
    sns.add(input())

suni = snh.intersection(sns)


print(len(suni))
sortedlist = sorted(suni)
ans = ""
for i in sortedlist:
    ans += i

print(ans)


