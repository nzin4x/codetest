c_t = int(input())
for i in range(c_t):
    c_q = int(input())
    wear = {}
    for q in range(c_q):
        _, kind = input().split()
        if kind in wear:
            wear[kind] = wear[kind] + 1
        else:
            wear[kind] = 1

    tot = 1
    for k in wear.keys():
        tot *= (wear[k] + 1)

    print(tot - 1)

