k = int(input())

n = 1000
a = [True] * n * n
a[0] = False
a[1] = False
t = 0
for i in range(2, n + 2):
    if a[i]:
        t += 1
        if t == k:
            print(i)
            break
        for j in range(i * i, n * n - 1, i):
            a[j] = False
else:
    print("-1")
