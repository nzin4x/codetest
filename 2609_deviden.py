num = int(input())

imin = 2
imax = num // 2
d = []

while True:
    if num % imin == 0:
        d.append(imin)
        num = num // imin
        if num == 1:
            break
    else:
        imin += 1
        if imin == imax:
            break

print(d)


