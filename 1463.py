min = 9999999
cnt = 0

def solve(x):
    if x == 1:
        return cnt

    by2 = x
    by3 = x

    cntby3 = 0
    cntby2 = 0
    while True:
        if by3 == 1:
            break
        elif by3 % 3 == 0:
            by3 = by3 // 3
            cntby3 += 1
            break
        else:
            cntby3 += 1
            by3 -= 1

    while True:
        if by2 == 1:
            break
        elif by2 % 2 == 0:
            by2 = by2 // 2
            cntby2 += 1
            break
        else:
            by2 -= 1
            cntby2 += 1

    solve(by3)
    solve(by2)

solve(2)
print(cnt)






