# dynamic programming bottom up

cache = {}
def strangemachine(x):
    cache[0] = [0, 0]
    cache[1] = [0, 1]
    for i in range(2, x + 1):
        pre = cache[i - 1]
        cache[i] = [pre[1], pre[0] + pre[1]]

    return str(cache[x][0]) + " " + str(cache[x][1])

print(strangemachine(int(input())))
