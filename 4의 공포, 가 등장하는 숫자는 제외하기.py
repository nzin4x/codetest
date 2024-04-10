target = 9876
fearcode = 4

current_target, next_target = target, target
while True:
    print(current_target)
    print('left new', str(current_target)[1:])
    if len(str(current_target)) == 1:
        break
    current_target = int(str(current_target)[1:])