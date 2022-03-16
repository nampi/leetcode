n = int(input())
a = list(map(int, input().split()))

max_elem = a[0]
max_idx = 0
for i in range(1, n):
    if max_elem > a[i]:
        max_elem = a[i]
        max_idx = i

print(max_idx)
