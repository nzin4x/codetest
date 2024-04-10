# 우선순위큐2개
# 큐 동기화
# 넣은 것에 대한 고유 번호를 튜플 2번째 값에 저장하고 이미 빠진 녀석인지 체크 하는 로직을 추가
import heapq
import sys

QC = int(sys.stdin.readline())

ans = ""
for _ in range(QC):
    hmax = []
    hmin = []
    iQC = int(sys.stdin.readline())

    removed = [False for _ in range(iQC + 1)]

    for i in range(iQC):
        C, N = sys.stdin.readline().split()
        # print(C,N)
        if C == "I":
            heapq.heappush(hmax, (-int(N), i))
            heapq.heappush(hmin, (int(N), i))
        elif C == "D":
            if N == "-1" and hmin:
                while hmin and removed[hmin[0][1]]:
                    heapq.heappop(hmin)
                if hmin:
                    removed[hmin[0][1]] = True
                    heapq.heappop(hmin)
            elif N == "1" and hmax:
                while hmax and removed[hmax[0][1]]:
                    heapq.heappop(hmax)
                if hmax:
                    removed[hmax[0][1]] = True
                    heapq.heappop(hmax)

        # if len(hmax) > 0:
        #     # print(-hmax[0], hmin[0])
        #     pass

    while hmin and removed[hmin[0][1]]: heapq.heappop(hmin)
    while hmax and removed[hmax[0][1]]: heapq.heappop(hmax)

    if len(hmin) == 0 or len(hmax) == 0:
        ans += "EMPTY\n"
    else:
        ans += str(-hmax[0][0]) + ' ' + str(hmin[0][0]) + "\n"

print(ans)
