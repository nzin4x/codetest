import sys

Q = int(sys.stdin.readline())
s = 0
ans = ""
full = (1 << 21) - 1
for i in range(Q):
    C = sys.stdin.readline().strip().split()
    n = 0

    if len(C) > 1:
        n = int(C[1])
    cmd = C[0]

    if cmd == "add":
        # 해당 자리를 1 로 채운다.
        s |= (1 << n)
    elif cmd == "check":
        # 해당 자리만 1로 (나머진 0) 채워진 것을 & 연산하면 모두 0 해당 자리의 값이 1이라 겹치면 0이 아닌 숫자가 된다. 있으면 0이 아니다.
        if s & (1 << n) != 0:
            # ans += "1\n"
            sys.stdout.write("1\n")
        else:
            # ans += "0\n"
            sys.stdout.write("0\n")
    elif cmd == "remove":
        s &= ~(1 << n)
    elif cmd == "toggle":
        s ^= (1 << n)
    elif cmd == "all":
        s = full
    elif cmd == "empty":
        s = 0

    # if i % 10001:
    #     print(ans)
    #     ans = ""

# print(ans)
