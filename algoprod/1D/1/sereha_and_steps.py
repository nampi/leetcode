n = int(input())
a = list(map(int, input().split()))
max_num = 5000
b = [0] * max_num
for x in a:
    b[x - 1] += 1

s = ""
t = 0
isFirst = False
for i in range(max_num - 1, -1, -1):
    if b[i] == 0:
        continue
    if not isFirst:
        s = str(i + 1)
        isFirst = True
        t += 1
        continue
    s += " " + str(i + 1)
    t += 1
    if b[i] > 1:
        s = str(i + 1) + " " + s
        t += 1
print(t)
print(s)
