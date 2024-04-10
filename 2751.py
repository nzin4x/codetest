import sys

input = sys.stdin.readline
print = sys.stdout.write


cnt = int(input())
l = []
for i in range(cnt):
    l.append(int(input()))

l = sorted(l)

ans = ""
for i in l:
    ans += str(i) + "\n"

print(ans)