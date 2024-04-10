n, k = map(int,input().split())
# print(type(k))
numbers = list(input())
ans = []
cnt = k

for num in numbers:
    while len(ans) > 0 and cnt > 0 and ans[-1] < num: # 스텍 맨 위의 것만 관심 있다.
        del ans[-1]
        cnt -= 1
    ans.append(num)

print(ans)

