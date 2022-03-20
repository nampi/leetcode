n = int(input())
a = [0] * max(4, n + 1)
a[0] = 0
a[1] = a[0] + 1
a[2] = a[0] + a[1] + 1
a[3] = a[0] + a[1] + a[2] + 1
for i in range(4, n + 1):
    a[i] = a[i - 3] + a[i - 2] + a[i - 1]

print(a[n])
