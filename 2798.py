#bruteforce algo
numcnt, imax = map(int, input().split())
nums = list(map(int,input().split()))
near = 0

# nums.sort()

for x in range(numcnt):
    for y in range(numcnt):
        for z in range(numcnt):
            if x == y or y == z or z == x:
                continue
            snum = nums[x] + nums[y] + nums[z]
            if (imax < snum):
                continue
            else:
                if(snum > near):
                    near = snum

print(near)



