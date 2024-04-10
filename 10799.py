q = input()
st = []
cnt = 0

for i in range(len(q)):
    if q[i] == '(':
        if q[i+1] == ')':
            # cutter
            cnt += len(st)
        else:
            # add
            st.append('.')
            cnt += 1
    elif q[i] == ')': #close
        if q[i - 1] == '(': # for cutter
            continue
        else:
            st.pop()

print(cnt)
