# stack but queue
from collections import deque

qc = int(input())
ans = ""

for i in range(qc):
    q = deque([])
    s = input()
    ok = True
    for l in range(len(s)):
        if s[l] == "(":
            q.append(s[l])
        elif s[l] == ")":
            if (len(q) > 0):
                check = q.pop()
                if check != "(":
                    ok = False
                    break
            else:
                ok = False
                break

    if ok and len(q) == 0:
        ans += "YES\n"
    else:
        ans += "NO\n"

print(ans)


