n, m = map(int, input().split())
a = list(map(int, input().split()))

prev = [0] * (n + 1)
prev[0] = 0
for i in range(1, n + 1):
    prev[i] = prev[i - 1] + a[i - 1]

for _ in range(m):
    x, y = map(int, input().split())
    print(prev[y] - prev[x - 1])
