s = input()

mode = 0 # 0 - no mode, 1 - eyes, 2 - nose, 3 - mouse
count = 0
for c in s:
    if c in ":;":
        mode = 1
    elif c == "-":
        if mode == 1 or mode == 2:
            mode = 2
        else:
            mode = 0
    elif c in "()[]":
        if mode == 1 or mode == 2:
            count += 1
        mode = 0
    else:
        mode = 0

print(count)
