n = int(input())
a = list(map(int, input().split()))

pref = [0] * (n + 1)
pref[0] = 0
for i in range(1, n + 1):

    pref[i] = pref[i - 1] + int(a[i - 1] == 0)

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    print(pref[y] - pref[x - 1], end=" ")
