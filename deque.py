from collections import deque
q = deque([])

q.append(1)
q.append(3)
q.popleft()
q.appendleft(4)

print(q)