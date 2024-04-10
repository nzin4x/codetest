import math
# 10은 5와 2가 만나면 된다. 2는 5보다 더 많이 등장한다.
# 5를 만나면 1개 추가 25를 만나면 2개, 125를 만나면 3개를 추가하면 된다.

n = int(input())

mult = 1
cnt0 = 0
for i in range(1, n+1):
    mult *= i

    # 짝수 * 짝수 = 짝수
    # 홀수 * 홀수 = 홀수
    # mult = mult % 10000

    if i % 5 == 0 or i % 10 == 0:
        # print(mult)
        while mult % 10 == 0:
            mult = mult // 10
            cnt0 += 1

    #print(i, cnt0)
    # print(i, mult)
    # print()

print(cnt0)


