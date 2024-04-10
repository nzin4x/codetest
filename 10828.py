line = int(input())
cmds = [input() for _ in range(line)]

st = []
for i in range(line):
    cmd = cmds[i].split()
    cm = cmd[0]

    if cm == 'push':
        st.append(cmd[1])
    elif cm == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop(-1))
    elif cm == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
    elif cm == 'size':
        print(len(st))
    elif cm == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)


