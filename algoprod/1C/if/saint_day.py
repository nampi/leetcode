a, b = map(int, input().split())

k = 0
flag = False
if b < 1605:
    k = 0
    flag = True
elif b == 1605:
    k = 1
    flag = True

if not flag:
    if b % 10 < 5:
        b = b - b % 10
    else:
        b = b - b % 10 + 10

    if a <= 1604:
        a = 1600
    elif a % 10 < 5:
        a = a - a % 10
    else:
        a = a - a % 10 + 10
    k = (b - a) // 10

print(k)
