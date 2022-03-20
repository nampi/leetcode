_ = input()
a = list(map(int, input().split()))
_ = input()
b = list(map(int, input().split()))
flag = True
for x in b:
    a[x - 1] -= 1
for x in a:
    if x >= 0:
        print("no")
    else:
        print("yes")
