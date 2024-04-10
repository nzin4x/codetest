nums = [list(map(int, input().split())) for _ in range(5)]

points = [0] * 5
maxi = 0
for y in range(5):
    for x in range(4):
        points[y] += nums[y][x]
        # print(points)

    maxi = max(maxi, points[y])


for y in range(5):
    if points[y] == maxi:
        print(y + 1, maxi)
