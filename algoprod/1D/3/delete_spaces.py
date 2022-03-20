s = input()
t = ""
isSpaceMode = False
for c in s:
    if c != " ":
        isSpaceMode = False
        t += c
        continue
    if not isSpaceMode:
        t += " "
        isSpaceMode = True
print(t)
