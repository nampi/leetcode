n, m = map(int, input().split())
all_good = 0
a = n * [0]
for i in range(m):
    s = input()
    num = -1
    for j in range(n):
        if s[j] == '+':
            if num == -1:
                num = j
            else:
                num = -1
                break
    if num != -1:
        all_good += 1
        a[num] += 1


for i in range(n):
    if 100 * a[i] >= 7 * all_good:
        print(i + 1, end=" ")
