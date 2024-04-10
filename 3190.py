import copy
import itertools
from collections import deque

n = int(input()) ## nxn size
applecnt = int(input()) ## apple cnt
apples = [list(map(int, input().split())) for _ in range(applecnt)]

directioncnt = int(input()) ## directions
cmds = [list(input().split()) for _ in range(directioncnt)]

# init
dq = deque([[1,1]])
# print('start dq : ' + str(dq))
direction = 'R'
cnt = 0

# start
def dead(dq):
    head = dq[-1]
    if head[0] > n or head[1] > n or head[0] < 1 or head[1] < 1:
        # print('wall')
        return True

    for i in range(len(dq) - 1):
        if dq[i] == head:
            # print('self eat')
            return True

    return False


def eat():
    head = dq[-1]
    for i in range(len(apples)):
        if head == apples[i]:
            del apples[i]
            return True
    return False

for cmd in cmds:
    while cnt < int(cmd[0]) or cmd == cmds[-1]:
        next = copy.copy(dq[-1])
        if direction == 'R':
            next[1] = next[1] + 1
        elif direction == 'L':
            next[1] = next[1] - 1
        elif direction == 'U':
            next[0] = next[0] - 1
        elif direction == 'D':
            next[0] = next[0] + 1

        # print('next : ' + str(next))
        # print('what is x : ', x)
        cnt += 1
        dq.append(next)

        if dead(dq):
            print(cnt)
            break
        # print('cnt : ' + str(cnt))
        # print('dq before check eat : ' + str(dq))
        if not eat():
            dq.popleft()
        else:
            pass
        # print('cnt : ', cnt, 'cmd[0] : ' , cmd[0],', dq : ' + str(dq))

        if cnt == int(cmd[0]):
            if cmd[1] == 'D' and direction == 'R': direction = 'D'
            elif cmd[1] == 'D' and direction == 'L': direction = 'U'
            elif cmd[1] == 'D' and direction == 'U': direction = 'R'
            elif cmd[1] == 'D' and direction == 'D': direction = 'L'
            elif cmd[1] == 'L' and direction == 'R': direction = 'U'
            elif cmd[1] == 'L' and direction == 'L': direction = 'D'
            elif cmd[1] == 'L' and direction == 'U': direction = 'L'
            elif cmd[1] == 'L' and direction == 'D': direction = 'R'

            # print('cnt ', cnt, ' turn with ', cmd[1], 'and direction to ', direction)



    if dead(dq):
        break









