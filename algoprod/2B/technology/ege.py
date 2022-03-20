s = input()

flag = True
num = ""
for c in s:
    if "0" <= c and c <= "9":
        num += c
    else:
        if num:
            n = int(num)
            if n > 5:
                flag = False
                break
        num = ""
if num:
    n = int(num)
    if n > 5:
        flag = False

if flag:
    print("YES")
else:
    print("NO")

