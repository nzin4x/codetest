while True:
    ns = list(map(int, input().split()))
    if ns[0] == 0:
        break
    ns.sort()
    if pow(ns[2], 2) == pow(ns[0],2) + pow(ns[1], 2):
        print("right")
    else:
        print("wrong")
