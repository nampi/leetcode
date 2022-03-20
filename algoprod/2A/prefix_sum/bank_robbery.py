n, k = map(int, input().split())
a = list(map(int, input().split()))
pref = [0] * (n + 1)
suff = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = max(pref[i - 1], a[i - 1])
for i in range(n - 1, -1, -1):
    suff[i] = max(suff[i + 1], a[i])

pref_ind = 0
suff_ind = 0
max_sum = 0
for i in range(0, n - k - 1):
    s = pref[i + 1] + suff[i + k + 1]
    if s > max_sum:
        max_sum = s
        pref_ind = i + 1
        suff_ind = i + k + 1

x, y = 0, 0
for i in range(0, pref_ind + 1):
    if a[i] == pref[pref_ind]:
        x = i
        break
for i in range(suff_ind, n):
    if a[i] == suff[suff_ind]:
        y = i
        break
print(x + 1, y + 1)
