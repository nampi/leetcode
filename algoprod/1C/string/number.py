n = int(input())
s = str(n)
pos = len(s) % 3
if pos == 0:
    pos = 3
for i in range(len(s)):
    print(s[i], end="")
    pos -= 1
    if i == len(s) - 1:
        break
    if pos == 0:
        print(",", end="")
        pos = 3
