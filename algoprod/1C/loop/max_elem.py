n = int(input())
a = list(map(int, input().split()))

maxElem = a[0]
for x in a:
    maxElem = max(maxElem, x)

print(maxElem)
