from collections import deque

N, K = map(int, input().split())
types = [0 for _ in range(N)]
used = set()
coins = 0
print(len(types))

for i in range(N):
    types[i] = int(input())

print(types)
types = deque(types)
while K > 0:
    tryn = types.pop()
    # print(f'lets try with {tryn}')
    if tryn > K:
        continue

    while K >= 0:
        K -= tryn
        used.add(tryn)
        # print(f'now set is {used}')
        coins+= 1
    K += tryn
    coins -= 1
    # print(f'K is {K} with {tryn}')


print(coins)



