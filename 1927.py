# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
import heapq
import sys

q = []

qc = int(input())
ans = ""
for i in range(qc):
    z = int(sys.stdin.readline())
    if z == 0:
        if len(q) == 0:
            ans += "0\n"
        else:
            ans += str(heapq.heappop(q)) + "\n"
    else:
        heapq.heappush(q, z)

print(ans)

