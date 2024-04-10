n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

# mp = []
# for i in len(range(ms)):
#     map[i] = ms[i]

mapms = {}
found = {}
for i in range(len(ms)):
    mapms[ms[i]] = i

sns = sorted(ns)
sms = sorted(ms)

pns = 0
for i in range(len(sms)):

    if sms[i] not in found:
        found[sms[i]] = 0

    while pns < len(sns):
        if sns[pns] < sms[i]:
            pns += 1
            continue
        elif sns[pns] == sms[i]:
            pns += 1
            found[sms[i]] = 1
        else:
            break


for i in range(len(ms)):
    # print('print for ', i, ' value ', ms[i])
    if found[ms[i]] == 1:
        print(1)
    else:
        print(0)







