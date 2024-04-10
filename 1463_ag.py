# dynamic programming bottom up

qc = int(input())

arr = [0] * (qc + 1)

def deepsearch(x):
    arr[1] = 0 # 이미 1이다.

    for i in range(2, x + 1, 1): # 2부터 올라가면서 arr 를 채워 넣는다.

        arr[i] = arr[i - 1] + 1  # condition 3 : 마지막 케이스 먼저 숫자를 채워 넣는다.

        # 만약 2라면, 1 에 일단 1을 더해본 1 횟수 증가가 채워져 있다.
        if (i % 2 == 0):
            # 그치만 2로 나누어 떨어지기 때문에,
            # 1을 더해서 2가 되는 것과
            # 2로 나뉘어졌던 값에서 1회 추가 하는 것중에 작은 것을 찾는다.

            # 4라면, 3에서 1을 더한 것과
            # 4의 반까지 걸린 횟수에 1 횟수를 추가한것과 비교하여 작은 것을 기록한다.
            arr[i] = min(arr[i], arr[i // 2] + 1)
        if (i % 3 == 0):
            # 3 이라면, 2에서 1만 추가 된 것과
            # 3으로 나누어 떨어졌던 것에 1회 추가 한 것과 비교하여 작은 것을 저장한다.
            arr[i] = min(arr[i], arr[i // 3] + 1)


deepsearch(qc)
print(arr[qc])
