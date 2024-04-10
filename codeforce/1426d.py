cq = int(input())
qs = list(map(int, input().split()))

ans = 0
s = set()
# incremental sum
isum = [0]*200000

s.add(0)
for i in range(cq):
    isum[i] = qs[i]
    if i != 0:
        isum[i] += isum[i-1]
    if isum[i] in s:
        ans += 1
        s.clear()
        s.add(isum[i-1])
    s.add(isum[i])

print(ans)

