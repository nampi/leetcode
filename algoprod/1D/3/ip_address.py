s = input()
a = s.split(".")
flag = True
for x in a:
    if x == "":
        flag = False
        break
    num = int(x)
    if num < 0 or num > 255:
        flag = False
        break
print(int(flag))
