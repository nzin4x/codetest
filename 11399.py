import sys

C = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = sorted(A)
# print(A)

sum = 0
iv = 0

for v in A:
    iv += v
    # print("iv", iv)
    sum += iv

print (sum)
