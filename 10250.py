qcnt = int(input())


def solve():
    h, w, t = map(int, input().split())

    d = t // h  # left 갯수 : 호수 XX
    r = t % h  # left 에서 높이  : 층수 YY

    if r == 0:
        return ("%d%02d\n" % (h, d))
    else:
        return ("%d%02d\n" % (r, d + 1))


ans = ""
for i in range(qcnt):
    ans += solve()

print(ans)
