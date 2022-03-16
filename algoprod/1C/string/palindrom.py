s = input()
flag = True
i, j = 0, len(s) - 1
while i < j:
    if s[i] == " ":
        i += 1
        continue
    if s[j] == " ":
        j -= 1
        continue
    if s[i] != s[j]:
        flag = False
        break
    i += 1
    j -= 1

if flag:
    print("yes")
else:
    print("no")
