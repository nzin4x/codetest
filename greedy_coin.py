# 그리디로 거스름돌 돌려주기

tgt = 1260
coins = [500,100,50,10]
cnt = 0

for coin in coins:
    cnt += tgt // coin
    tgt = tgt % coin

print(cnt)