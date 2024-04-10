# fibo compare

fib1cnt = 0
fibdpcnt = 0

def fib1(n):
    global fib1cnt
    if n == 1 or n == 2:
        fib1cnt += 1
        return n
    else:
        return fib1(n - 2) + fib1(n - 1)

mem = {}
def fib2(n):
    global fibdpcnt
    mem[1] = 1
    mem[2] = 1

    for i in range (3, n + 1):
        fibdpcnt += 1
        mem[i] = mem[i - 2] + mem[i - 1]

    return mem[n]

m2 = {}
def fib1cnt(n):
    m2[1] = 1
    m2[2] = 1
    for i in range(3, n + 1):
        m2[i] = m2[i - 2] + m2[i - 1]

    return m2[n]

x = int(input())

# fib1(x)
# fib1cnt(x)
# fib2(x)
print(fib1cnt(x), x - 2)