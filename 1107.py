D = False

asis = 100
tobe = int(input())
brokencnt = int(input()) #bypass
notworkingmap = ""

workingpad = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
if brokencnt > 0:
    notworkingmap = input()
    c = list(map(int, notworkingmap.split()))
    for x in c:
        workingpad.discard(x)

if D:print('tobe', tobe)
if D:print('broken count', brokencnt)
if D:print('workingpad', workingpad)

min_input = abs(asis - tobe)
for N in range(0, max(tobe,asis) * 2 + 1):
    if D:print('lets test with', N, 'and the set is', set(list(str(N))))
    if set(map(int,str(N))) <= workingpad:
        if D:print('working number')
        min_input = min(abs(N - tobe) + len(str(N)), min_input)
        if D:print('current min!', min_input)
    else:
        if D:print('not working number')

print (min_input)