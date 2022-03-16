n = int(input())
a = list(map(int, input().split()))

maxElem = a[0]
maxIdx = 0
for i in range(1, n):
    if maxElem > a[i]:
        maxElem = a[i]
        maxIdx = i

print(maxIdx)
