import sys

N, M = map(int, sys.stdin.readline().split()) # number of trees, target top
T = list(map(int, sys.stdin.readline().split()))

# print(N)
# print(M)
# print(T)

# 4 개 중에서 7만큼을 얻고 싶다면, 1씩 짤라보고 2씩 짤라보고 할텐데, 일단 max 를 알아야 몇으로 짤라 볼 지 알 수 있을 듯

T = sorted(T,reverse=True)

max_tall = T[0]
min_tall = T[len(T) - 1]
trees = T
cutter = 1
target = M
correct_cutter = 0

avg_tall = int(sum(T) / len(T))
cutter = avg_tall
prev_cutter = cutter

while True:
    sum = 0
    print('current cutter : ', cutter)
    for tree in trees:

        if tree > cutter:
            sum = sum + tree - cutter
        elif tree < cutter:se:
            break


    if sum == target:
        correct_cutter = cutter
        break
    elif sum > target:
        # increase cutter to decrease target
        prev_cutter = cutter
        cutter = int((cutter + max_tall) / 2)
    else:
        # decrease cutter to increase target
        prev_cutter = cutter
        cutter = int((cutter + min_tall) / 2)

print(correct_cutter)



