# 사실상 피보나치
n = int(input())
# n = 8
cache = [0 for _ in range(n + 2)]

cache[0] = 0
cache[1] = 1
cache[2] = 2

sum = 0
def fibo(n):
    global sum
    for i in range(3, n + 1):
       cache[i] = cache[i-2] + cache[i-1]

k = fibo(n)
print(cache[n] % 10007)

# 1 2 3 5 8 13 21 34 55
# 1 2 3 4 5 6  7  8  9  10
