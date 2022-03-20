
s = input()
t = input()

mapping = {}
for c in s:
    if c in mapping:
        mapping[c] += 1
    else:
        mapping[c] = 1
flag = True
for c in t:
    if c in mapping:
        if mapping[c] > 0:
            mapping[c] -= 1
        else:
            flag = False
            break
    else:
        flag = False
        break
if len(s) == len(t) and flag:
    print("YES")
else:
    print("NO")