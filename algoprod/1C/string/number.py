s = input()

pos = len(s) % 3
if pos == 0:
    pos = 3

for c in s:
    if pos == 0:
        print(",", end="")
        pos = 3
    print(c, end="")
    pos -= 1
