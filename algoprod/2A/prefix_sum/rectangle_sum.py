n, m, k = map(int, input().split())

# Как лучше создавать матрицу и считывать в нее значения?
a = [[0] * m for row in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

pref = [[0] * (m + 1) for row in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i - 1][j - 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(pref[x2][y2] - pref[x2][y1 - 1] - pref[x1 - 1][y2] + pref[x1 - 1][y1 - 1])
