import sys

Q = int(sys.stdin.readline())
s = set()
ans = ""
for _ in range(Q):
    C = sys.stdin.readline().split()
    n = 0
    if len(C) > 1:
        n = int(C[1])
    cmd = C[0]

    # print("cmd", cmd, n)

    if cmd == "add":
        s.add(n)
    elif cmd == "check":
        if n in s:
            # ans += "1\n"
            sys.stdout.write("1\n")
        else:
            # ans += "0\n"
            sys.stdout.write("0\n")
    elif cmd == "remove":
        if n in s:
            s.remove(n)
    elif cmd == "toggle":
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif cmd == "all":
        for v in range(1,20 + 1):
            s.add(v)
    elif cmd == "empty":
        s.clear()

print(ans)

