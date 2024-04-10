# 유클리드 호제법

a, b = list(map(int, input().split()))

# a = 6, b = 8
if a < b:
    a, b = b, a

while True:
    # a = 8, b = 6
    # r = 2, a = 6, b = 2
    # r = 0, a, 2, b = 0

    if b != 0:
        r = a % b
        a = b
        b = r
    else:
        break

print (a)
