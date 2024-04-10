from heapq import *

array = [3,2,4]
heap = []
sarray = []

for i in range(len(array)):
    heappush(heap, array[i])

for i in range(len(array)):
    sarray.append(heappop((heap)))

print(sarray)

