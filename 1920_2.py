n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

s = set(ns)

r = []
for val in ms:
    if val in s:
        r.append('1')
    else:
        r.append('0')

print('\n'.join((r)))