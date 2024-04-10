from collections import deque

n = int(input())
q = deque(list(map(lambda x:x+1,list(range(n)))))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
