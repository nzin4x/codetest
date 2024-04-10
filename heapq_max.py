import heapq

h = []
lst = [2,3,4]
for v in lst:
    heapq.heappush(h, (-v, v))

print(h)