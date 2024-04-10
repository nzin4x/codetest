# fibonacci dynamic programming bottom up
solved = {}

def fibo(x):
    solved[0] = 0
    solved[1] = 1

    for i in range(2, x + 1):
        solved[i] = solved[i - 2] + solved[i - 1]

    return solved[x]

print(fibo(int(input())))

