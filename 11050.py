import sys

input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(n):
    multsum = 1
    for i in list(range(2, n + 1)):
        multsum *= i

    return multsum

print(str(int(factorial(n) / factorial(k) / factorial(n-k))))
