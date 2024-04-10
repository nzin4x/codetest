def cntx(n):
    x, y = 1, 0
    for i in range(n):

        k = y
        y = x + y
        x = k

    return (x, y)


qc = int(input())
ans = ""
for i in range(qc):
    x, y = cntx(int(input()))
    ans += str(x) + " " + str(y) + "\n"

print(ans)
