from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

qc = int(input())
q = deque([])
ans = ""
for i in range(qc):
    line = input().split()
    cmd = line[0]
    if cmd == "push_front":
        q.appendleft(line[1])
    elif cmd == "push_back":
        q.append(line[1])
    elif cmd == "pop_front":
        if len(q) == 0:
            ans += "-1\n"
        else:
            p = q.popleft()
            ans += p + "\n"
    elif cmd == "pop_back":
        if len(q) == 0:
            ans += "-1\n"
        else:
            p = q.pop()
            ans += p + "\n"
    elif cmd == "size":
        ans += str(len(q)) + "\n"
    elif cmd == "empty":
        if len(q) == 0:
            ans += "1\n"
        else:
            ans += "0\n"
    elif cmd == "front":
        if len(q) == 0:
            ans += "-1\n"
        else:
            ans += q[0] + "\n"
    elif cmd == "back":
        if len(q) == 0:
            ans += "-1\n"
        else:
            ans += q[-1] + "\n"

print(ans)




