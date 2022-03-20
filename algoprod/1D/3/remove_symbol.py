s = input()
a = list(s)
i, j = 0, 0
while j < len(a):
    if a[j] != "@":
        a[i], a[j] = a[j], a[i]
        i += 1
        j += 1
        continue
    j += 1

print("".join(a[0:i]))
